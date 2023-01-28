from tkinter import *

def create_triangle(canvas,x1,y1,x2,y2,x3,y3):
    canvas.create_line(x1,y1,x2,y2)
    canvas.create_line(x1,y1,x3,y3)
    canvas.create_line(x3,y3,x2,y2)