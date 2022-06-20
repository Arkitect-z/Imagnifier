from PIL import Image

img = Image.open("D:\Desktop/test.png")
rlt = img.resize((65,65),resample=Image.LANCZOS)
rlt.save("D:\Desktop/test1.png")
