from PIL import Image, ImageDraw

# Converts image to black, white and grey
# f = Image.open('test.png')
# f = f.convert('1')
# f.show()


# Also converts image to black, white and grey
# f = Image.open('test.png')
# pic = ImageDraw.Draw(f)
# width = f.size[0]
# heigth = f.size[1]
# pix = f.load()
# for i in range(width):
#     for j in range(heigth):
#         r = pix[i, j][0]
#         g = pix[i, j][1]
#         b = pix[i, j][2]
#         S = (r + g + b) // 3
#         pic.point((i, j), (S, S, S))
# f.save("testing.png", "PNG")

# To make picture black and white
# f = Image.open('testing.png')
# pic = ImageDraw.Draw(f)
# width = f.size[0]
# heigth = f.size[1]
# pix = f.load()
# for i in range(width):
#     for j in range(heigth):
#         if (pix[i, j][0] + pix[i, j][1] + pix[i,j][2]) > 384 :
#             S = 568
#         else :
#             S = 0
#         pic.point((i, j), (S, S, S))
# f.show()

# mirror reflection
# f = Image.open('test.png')
# pic = ImageDraw.Draw(f)
# width = f.size[0]
# heigth = f.size[1]
# pix = f.load()
# for i in range(width//2):
#     for j in range(heigth):
#         a, b, c = pix[i, j][0], pix[i, j][1], pix[i, j][2]
#         if i==0:
#             i+=1
#         pic.point((i, j), (pix[width - i, j][0], pix[width - i, j][1], pix[width - i, j][2]))
#         pic.point((width - i, j), (a, b, c))
# f.show()

# mirror reflection on y
f = Image.open('test.png')
pic = ImageDraw.Draw(f)
width = f.size[0]
height = f.size[1]
pix = f.load()
for i in range(width):
    for j in range(height//2):
        a, b, c = pix[i, j][0], pix[i, j][1], pix[i, j][2]
        if j==0:
            j += 1
        pic.point((i, j), (pix[i, height - j][0], pix[i, height - j][1], pix[i, height - j][2]))
        pic.point((i, height - j), (a, b, c))
f.show()