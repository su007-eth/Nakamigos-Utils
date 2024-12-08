# Nakamigos Utils

这是一个非官方的 Nakamigos 资源和工具库，包括原始 20,000 个 Nakamigos 的 PNG 图片，每个图片的像素数据,ExcelNakamigos等。图片资源来源于https://github.com/linxinglu/nakamigos-unofficial

## Nakamigos 资源

### 1. 原始图片（20k PNG）
- 资源位于 `data/images/`
- 有2000*2000像素和24*24像素两种大小
- 压缩包中图片命名：`0.png, 1.png, 2.png, ... 19999.png`

### 2. 像素数据
- 资源位于 `data/pixel_data/`
- 压缩包里有两种格式：CSV 和 TXT
- 总共有 20,000 行，每行对应一个图片的像素值（24×24 = 576 像素）
- 每个像素值是以 8 位十六进制RGBA格式表示的：`RRGGBBAA`
- 是使用 `src/get_pixels.py` 工具从 20k PNG 图片中提取的像素数据

## ExcelNakamigos

### 文件结构：
- 文件位于 `excel/ExcelNakamigos.xlsm`
- 打开是确保启用宏
- Excel 文件包含：
  - "Data" 工作表，存储像素数据
  - 24×24 的显示网格，用于查看 NFT
  - 两个名称引用：
    - `NFT_NUMBER`：要查看的 NFT ID
    - `NFT_START_NUM`：NFT 集合的起始 ID

### 如何填充绘制不同的 NFT：
  1. 修改 `NFT ID` 的值，点击'Draw'按钮，将自动根据图片像素值在 24×24 网格中填充颜色。
  2. 你可以点击上下箭头切换不同的 NFT
  3. 每个单元格的颜色代表 NFT 的一个像素

## 贡献

欢迎通过以下方式贡献：
1. 添加新工具或实用程序
2. 改进现有代码
3. 添加文档
4. 报告问题

## 许可

这是一个非官方工具库。所有 Nakamigos 图片和相关内容的所有权归其各自所有者所有。
