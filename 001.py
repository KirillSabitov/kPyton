from tkinter import *
window = Tk()

canvas = Canvas(window, width=200, height=200)
canvas.pack()
x = -20
canvas.create_polygon(50,200,50,150,40,150,100,100,160,150,150,150,150,200)
canvas.create_oval(140,40,170,70,width=1,fill='yellow')
while x < 200:
    canvas.create_arc(x, 170, x +40,250, outline='green',
    style=ARC, start= 180,extent=-80,
    width=2)
    x += 10

window.mainloop()