from tkinter import *

win = Tk()
ent1 = Entry(width=20)
ent2 = Entry(width=20)
bplus = Button(text='+')
bminus = Button(text='-')
bumn = Button(text='*')
bdel = Button(text='/')
lab = Label(width=20, bg='black',fg='white')

def plus(event):
    x1 = ent1.get()
    x1 = int(x1)
    x2 = ent2.get()
    x2 = int(x2)
    rez = str(x1 + x2)
    lab['text'] = rez

def minus(event):
    x1 = ent1.get()
    x1 = int(x1)
    x2 = ent2.get()
    x2 = int(x2)
    rez = str(x1 - x2)
    lab['text'] = rez

def umn(event):
    x1 = ent1.get()
    x1 = int(x1)
    x2 = ent2.get()
    x2 = int(x2)
    rez = str(x1 * x2)
    lab['text'] = rez

def delit(event):
    x1 = ent1.get()
    x1 = int(x1)
    x2 = ent2.get()
    x2 = int(x2)
    rez = str(x1 / x2)
    lab['text'] = rez


bplus.bind('<Button-1>',plus)
bminus.bind('<Button-1>',minus)
bumn.bind('<Button-1>',umn)
bdel.bind('<Button-1>',delit)

ent1.pack()
ent2.pack()
bplus.pack()
bminus.pack()
bumn.pack()
bdel.pack()
lab.pack()

win.mainloop()

