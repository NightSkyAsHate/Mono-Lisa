from tkinter import *

f = input('f(x):')

w = 1000
h = 500

max = 0
min = 0
first_x = -500
for i in range(1000):
    x = first_x + i
    f1 = f.replace('x',str(x))
    y1 = -eval(f1)
    if y1 > max:
        max = y1
    if y1 < min:
        min = y1;

if (abs(max) > abs(min)):
    h = abs(max)
    h_min = min
else:
    h = abs(min)
    h_min = max

if (h_min < -500):
        h_min = -500;
if (h > 500):
        h = 500;

h_min -= 50
h += 50
h_length = h - h_min

if (h_length > 1000):
    h_length = 1000

root = Tk()

canvas = Canvas(root, width=1000, height=h_length, bg='lightblue', cursor='pencil')
canvas.create_line(h, w, h, 0, width=2, arrow=LAST)
canvas.create_line(0, h, w, h, width=2, arrow=LAST)

First_x = -h

print(h)
for i in range(int(h_length)):
    k = First_x + i;
    if i % 10 == 0:
        canvas.create_line(-3 + h, k + h, 3 + h, k + h, width=0.5, fill='black')
        canvas.create_text(20 + h, k + h, text=str(int(k)), fill="purple", font=("Helvectica", "10"))



for i in range(16000):
    if i % 800 == 0:
        k = First_x + (1 / 16) * i
        canvas.create_line(k + h, -3 + h, k + h, 3 + h, width=0.5, fill='black')
        canvas.create_text(k + h + 15, -10 + h, text=str(int(k)), fill="purple", font=("Helvectica", "10"))
        # if k != 0:
        #     canvas.create_line(-3 + h, k + h, 3 + h, k + h, width=0.5, fill='black')
        #     canvas.create_text(20 + h, k + h, text=str(k), fill="purple", font=("Helvectica", "10"))
    try:
        x = First_x + (1 / 16) * i
        new_f = f.replace('x', str(x))
        y = -eval(new_f) + h
        x += h
        canvas.create_oval(x, y, x + 1, y + 1, fill='black')
    except:
        pass

canvas.pack()
root.mainloop()