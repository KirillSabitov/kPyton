from tkinter import *
window = Tk()

canvas = Canvas(window, width=200, height=200)
canvas.pack()
x = -20


while x < 200:
    canvas.create_arc(x, 170, x +40,250, outline='green',
    style=ARC, start= 180,extent=-80,
    width=2)
    x += 10

window.mainloop()