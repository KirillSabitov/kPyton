from tkinter import * 

def q():
    lab['bg'] = 'red'
def w():
    lab['bg'] = 'green'
def e():
    lab['bg'] = 'blue'

root = Tk()

var = IntVar()
var.set(0)

red = Radiobutton(text='Красный',variable=var, value=0,command=q)
green = Radiobutton(text='Зеленый',variable=var, value=1,command=w)
blue = Radiobutton(text='Синий',variable=var, value=2,command=e)

lab = Label(width=20,height=10)
red.pack()
green.pack()
blue.pack()

lab.pack()

root.mainloop()