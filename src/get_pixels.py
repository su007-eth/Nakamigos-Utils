import numpy as np
from PIL import Image
import pandas as pd
import os
import glob

def process_image(image_path):
    """处理单个图片，提取RGBA像素值"""
    img = Image.open(image_path)
    img = img.convert('RGBA')
    img_array = np.array(img)
    
    # 将RGBA值转换为单个16进制数字
    hex_values = (img_array[:, :, 0].astype(np.uint32) << 24 | 
                 img_array[:, :, 1].astype(np.uint32) << 16 | 
                 img_array[:, :, 2].astype(np.uint32) << 8  | 
                 img_array[:, :, 3].astype(np.uint32))
    
    return hex_values.flatten()

def get_image_files(image_dir, pattern='*.png'):
    """获取指定目录下的所有图片文件，并按文件名数字排序"""
    files = glob.glob(os.path.join(image_dir, pattern))
    
    # 提取文件名中的数字部分进行排序
    def extract_number(file_path):
        filename = os.path.splitext(os.path.basename(file_path))[0]
        try:
            return int(filename)
        except ValueError:
            # 如果文件名不是纯数字，则放在最后
            return float('inf')
    
    files.sort(key=extract_number)
    return files

def main():
    # 配置参数
    image_dir = 'images'  # 图片目录
    pattern = '*.png'         # 文件匹配模式
    csv_file = 'pixels_data.csv'      # CSV输出文件
    txt_file = 'pixels_data.txt'          # 文本输出文件
    batch_size = 500                 # 进度显示间隔
    
    # 检查目录是否存在
    if not os.path.exists(image_dir):
        print(f"错误：找不到 {image_dir} 目录！")
        return
    
    # 获取所有图片文件
    image_files = get_image_files(image_dir, pattern)
    if not image_files:
        print(f"错误：在 {image_dir} 目录下没有找到任何 {pattern} 文件！")
        return
    
    total_files = len(image_files)
    print(f"找到 {total_files} 个图片文件")
    print("开始处理图片...")
    
    # 处理所有图片
    all_data = []
    file_ids = []  # 存储文件名（不含扩展名）
    processed_files = 0
    
    for image_path in image_files:
        try:
            hex_values = process_image(image_path)
            all_data.append(hex_values)
            # 提取文件名（不含扩展名）作为ID
            file_id = os.path.splitext(os.path.basename(image_path))[0]
            file_ids.append(file_id)
            
            processed_files += 1
            if processed_files % batch_size == 0:
                print(f"已处理 {processed_files}/{total_files} 个文件...")
                
        except Exception as e:
            print(f"处理图片 {image_path} 时出错: {e}")
    
    print(f"找到并处理了 {processed_files} 个文件")
    
    if not all_data:
        print("没有成功处理任何文件！")
        return
    
    # 1. 保存为CSV格式
    print("\n保存CSV格式...")
    df = pd.DataFrame(all_data)
    
    # 将数值转换为16进制字符串
    for col in df.columns:
        df[col] = df[col].map(lambda x: f'{x:08X}')
    
    # 添加文件编号列
    df = pd.concat([pd.Series(file_ids, name='file_id'), df], axis=1)
    
    # 保存CSV文件
    df.to_csv(csv_file, index=False)
    print(f"CSV数据已保存到 {csv_file}")
    print(f"数据形状: {df.shape[0]},{df.shape[1]-1}(文件数 x 像素数)")
    
    # 2. 保存为紧凑格式
    print("\n保存紧凑格式...")
    # 删除file_id列并合并每行
    text_data = df.drop('file_id', axis=1).apply(lambda row: ''.join(row), axis=1)
    
    # 保存文本文件
    with open(txt_file, 'w') as f:
        f.write('\n'.join(text_data))
    
    print(f"紧凑格式数据已保存到 {txt_file}")
    print(f"处理完成！每个图片包含 {df.shape[1]-1} 个像素")

if __name__ == "__main__":
    main()
