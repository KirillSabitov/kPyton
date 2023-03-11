from tkinter import *
root = Tk()
fr_top = Frame(root)


lab = Label(fg='black')
e1 = Entry(width=50)
b1 = Button(fr_top,bg='#ff0000')
b2 = Button(fr_top,bg='#ff7d00')
b3 = Button(fr_top,bg='#ffff00')
b4 = Button(fr_top,bg='#00ff00')
b5 = Button(fr_top,bg='#007dff')
b6 = Button(fr_top,bg='#0000ff')
b7 = Button(fr_top,bg='#7d00ff')
def red():
    e1.delete(0,END)
    lab['text'] = 'Красный'
    e1.insert(END,'                                           #ff0000     ')
def orange():
    e1.delete(0,END)
    lab['text'] = 'оранжевый'
    e1.insert(END,'                                           #ff7d00     ')
def yel():
    e1.delete(0,END)
    lab['text'] = 'желтый'
    e1.insert(END,'                                           #ffff00     ')
def green():
    e1.delete(0,END)
    lab['text'] = 'зеленый'
    e1.insert(END,'                                           #00ff00     ')
def lblue():
    e1.delete(0,END)
    lab['text'] = 'голубой'
    e1.insert(END,'                                           #007dff     ')
def dblue():
    e1.delete(0,END)
    lab['text'] = 'синий'
    e1.insert(END,'                                           #0000ff     ')
def purp():
    e1.delete(0,END)
    lab['text'] = 'фиолетовый'
    e1.insert(END,'                                           #7d00ff     ')
b1.config(command=red)
b2.config(command=orange)
b3.config(command=yel)
b4.config(command=green)
b5.config(command=lblue)
b6.config(command=dblue)
b7.config(command=purp)

lab.pack()
e1.pack()
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
b4.pack(side=LEFT)
b5.pack(side=LEFT)
b6.pack(side=LEFT)
b7.pack(side=LEFT)
fr_top.pack()
root.mainloop()