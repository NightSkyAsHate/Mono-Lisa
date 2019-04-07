from PIL import Image, ImageDraw

f = Image.open('test.png')
pic = ImageDraw.Draw(f)
width = f.size[0]
height = f.size[1]
pix = f.load()
for i in range(width):
    for j in range(height):
        r = pix[i,j][0]
        g = pix[i,j][1]
        b = pix[i,j][2]
        S = (r + g + b)//3
        pic.point(lambda  i: 100 < i < 255)
f.show()