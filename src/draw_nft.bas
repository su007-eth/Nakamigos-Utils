Option Explicit

Sub RGBA()
    Dim ImageRGBA As String, s As String
    Dim i As Integer, j As Integer
    Dim R As Integer, G As Integer, B As Integer, A As Integer
    
    ' 从Nakamigos工作表获取像素数据
    ImageRGBA = Worksheets("Data").Cells([NFT_NUMBER]-[NFT_START_NUM]+1, 2)
    
    ' 清除24x24网格的所有颜色
    Range(Cells(1, 1), Cells(24, 24)).Interior.Pattern = xlNone
    
    ' 遍历24x24的像素网格
    For i = 1 To 24
        For j = 1 To 24
            ' 获取每个像素的8位16进制颜色值
            s = Mid(ImageRGBA, (i - 1) * 24 * 8 + (j - 1) * 8 + 1, 8)
            
            ' 提取透明度值
            A = Val("&H" & (Mid(s, 7, 2)))
            
            ' 如果不是透明的
            If A <> 0 Then
                ' 提取RGB值
                R = Val("&H" & (Mid(s, 1, 2)))
                G = Val("&H" & (Mid(s, 3, 2)))
                B = Val("&H" & (Mid(s, 5, 2)))
                
                ' 设置单元格颜色
                Range(Cells(i, j), Cells(i, j)).Interior.Color = RGB(R, G, B)
            End If
        Next j
    Next i
End Sub

Sub ChangeNum()
    RGBA
End Sub
