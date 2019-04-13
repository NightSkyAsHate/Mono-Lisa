from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk, ImageDraw
    
tk = None
def start():
    global tk
    def mirror():
        picT = ImageDraw.Draw(pic)
        width = pic.size[0]
        heigth = pic.size[1]
        pix = pic.load()
        for i in range(width//2):
            for j in range(heigth):
                a, b, c = pix[i, j][0], pix[i, j][1], pix[i, j][2]
                if i==0:
                    i+=1
                picT.point((i, j), (pix[width - i, j][0], pix[width - i, j][1], pix[width - i, j][2]))
                picT.point((width - i, j), (a, b, c))
        picTk = ImageTk.PhotoImage(pic)
        label.configure(image = picTk)
        label.image = picTk

    def grey():
        picT = ImageDraw.Draw(pic)
        width = pic.size[0]
        heigth = pic.size[1]
        pix = pic.load()
        for i in range(width):
            for j in range(heigth):
                r = pix[i, j][0]
                g = pix[i, j][1]
                b = pix[i, j][2]
                S = (r + g + b) // 3
                picT.point((i, j), (S, S, S))
        picTk = ImageTk.PhotoImage(pic)
        label.configure(image = picTk)
        label.image = picTk

    def blackAndWhite():
        picT = ImageDraw.Draw(pic)
        width = pic.size[0]
        heigth = pic.size[1]
        pix = pic.load()
        for i in range(width):
            for j in range(heigth):
                if (pix[i, j][0] + pix[i, j][1] + pix[i,j][2]) > 384 :
                    S = 568
                else :
                    S = 0
                picT.point((i, j), (S, S, S))
        picTk = ImageTk.PhotoImage(pic)
        label.configure(image = picTk)
        label.image = picTk

    def returnAsItWas():
        returnImage = Image.open(cult)
        picTk = ImageTk.PhotoImage(returnImage)
        label.configure(image = picTk)
        label.image = picTk

    def brown():
        picT = ImageDraw.Draw(pic)
        width = pic.size[0]
        height = pic.size[1]
        pix = pic.load()
        depth = 25
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                S = (a + b + c) // 3
                a = S + depth * 2
                b = S + depth
                c = S
                if a > 255:
                    a = 255
                if b > 255:
                    b = 255
                if c > 255:
                    c = 255
                picT.point((i, j), (a, b, c))
        picTk = ImageTk.PhotoImage(pic)
        label.configure(image = picTk)
        label.image = picTk

    def negative():
        picT = ImageDraw.Draw(pic)
        width = pic.size[0]
        heigth = pic.size[1]
        pix = pic.load()
        for i in range(width):
            for j in range(heigth):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                picT.point((i, j), (255 - a, 255 - b, 255 - c))
        picTk = ImageTk.PhotoImage(pic)
        label.configure(image = picTk)
        label.image = picTk

    tk = Tk()
    tk.title("Image editing")
    file = askopenfilename()
    pic = Image.open(file)
    cult = file
    picTk = ImageTk.PhotoImage(pic)
    label = Label(tk, image = picTk)
    label.image = picTk
    label.place(x = 0, y = 0)
    label.pack()
    turn90 = Button(tk, text = "mirror", command = lambda:mirror())
    turn90.pack(side = RIGHT)
    button = Button(tk, text = "grey", command = lambda:grey())
    button.pack(side = RIGHT)
    button1 = Button(tk, text = "black & white", command = lambda:blackAndWhite())
    button1.pack(side = RIGHT)
    button2 = Button(tk, text = "original", command = lambda:returnAsItWas())
    button2.pack(side = RIGHT)
    button3 = Button(tk, text = "brown", command = lambda:brown())
    button3.pack(side = RIGHT)
    button4 = Button(tk, text = "negative", command = lambda:negative())
    button4.pack(side = RIGHT)
    label.update()

start()
tk.mainloop()