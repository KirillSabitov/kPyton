from tkinter import *
from datetime import datetime as dt

def it():
    t = dt.now().time()
    e1.insert(END,t.strftime('%H:%M:%S  '))


root = Tk()
e1 = Entry(width=50)
but = Button(text='Время',command=it)

e1.pack()
but.pack()

root.mainloop()