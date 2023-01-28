from tkinter import *
from graf import create_triangle

window = Tk()
window.title('треугольник')
canvas = Canvas(window, width = 800, height=600,background='white')

x1 = input('Введите х координату первой точки           ')
y1 = input('Введите y координату первой точки           ')
x2 = input('Введите х координату второй точки           ')
y2 = input('Введите y координату второй точки           ')
x3 = input('Введите х координату третьей точки          ')
y3 = input('Введите y координату третьей точки          ')
create_triangle(canvas,x1,y1,x2,y2,x3,y3)

canvas.pack(expand=True,fill=BOTH)
window.mainloop()
