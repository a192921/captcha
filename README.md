# captcha
captcha in python


#PIL(Python Imaging Library)
- 為Python影像處理的擴展庫
- 需先獨立安裝才能使用
- 模組：Image、ImageChops、ImageColor、ImageDraw、ImagePath、ImageFile、ImageEnhance、PSDraw、ImageFont、ImageFilter、ImageMath、ImagePalette...等。

引用：https://pillow.readthedocs.io/en/latest/

由於PIL對Python3.x的支援不是很好，可以改用擴展庫pillow代替。
- 安裝pillow：pip install pillow
- 匯入模組：from PIL import Image
- 基本語法：
  - 開啟圖片檔：im = Image.open('檔案名稱')
  - 顯示圖形：im.show()
  - 查看圖片資訊：im.format、im.size、im.height、im.width


![驗證圖片1](https://github.com/a192921/captcha/blob/master/result.jpg)

![驗證圖片2](https://github.com/a192921/captcha/blob/master/result-1.jpg)
