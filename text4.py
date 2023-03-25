from tkinter import *

def open_file():
    if e1.get()!='':
        with open(e1.get(),'r') as f1:
            rtext = f1.read()
            text.delete(1.0,END)
            text.insert(1.0,rtext)

def save_file():
    if e1.get()!='':
        rtext = text.get('1.0',END)
        with open(e1.get(),'w') as f1:
            f1.write(rtext)

root = Tk

fr1 = Frame()
e1 = Entry(fr1,width=20)
b1 = Button(fr1,text='Открыть',width=15,height=1,command=open_file)
b2 = Button(fr1,text='Сохранить',width=15,height=1,command=save_file)
text = Text(width=50, height=7)
e1.pack(side=LEFT)
b1.pack(side=LEFT)
b2.pack(side=LEFT)
fr1.pack()
text.pack()
root.mainloop()