from tkinter import *

root = Tk
c =Canvas(root, width = 800, height=600)
def addFigure():
    fig = Toplevel()
    fig.title('Фигура')
    fig.resizable(0,0)


    Label(text='x1').grid(fig,row=0, column=0, sticky=W,pady=10,padx=10)
    x1 = Entry(width=3)
    x1.grid(fig,row=0, column=1, sticky=W,pady=10,padx=10)
    Label(text='y1').grid(fig,row=0, column=2, sticky=E,pady=10,padx=10)
    y1 = Entry(width=3)
    y1.grid(fig,row=0, column=3, sticky=E,pady=10,padx=10)

    Label(text='x2').grid(fig,row=1, column=0, sticky=W,pady=10,padx=10)
    x2 = Entry(width=3)
    x2.grid(fig,row=1, column=1, sticky=W,pady=10,padx=10)
    Label(text='y2').grid(fig,row=1, column=3, sticky=E,pady=10,padx=10)
    y2 = Entry(width=3)
    y2.grid(fig,row=1, column=4, sticky=E,pady=10,padx=10)

    v = IntVar()
    v.set(1)
    Radiobutton(text='Прямоугольник',variable=v,value=1).grid(fig,row=2, column=0,columnspan=3,sticky=W,padx=10)
    Radiobutton(text='Овал',variable=v,value=0).grid(fig,row=3, column=0,columnspan=3,sticky=W,padx=10)

    def paint():
        x = int(x1.get())
        y = int(y1.get())
        xx = int(x2.get())
        yy = int(y2.get())
        if v.get() == 0:
            c.create_oval(x,y,xx,yy,width=2 )
        if v.get() == 1:
            c.create_rectangle(x,y,xx,yy,width=2)

