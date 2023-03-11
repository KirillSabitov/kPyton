from tkinter import *

root = Tk()

fr_top = LabelFrame(root,text='Первый')
fr_bot = LabelFrame(root,text='Dnj')
l1 = Label(fr_top,width=7,height=4,text='1')
l3 = Label(fr_top,width=7,height=4,text='2')
l2 = Label(fr_bot,width=7,height=4,text='3')
l4 = Label(fr_bot,width=7,height=4,text='4')

l1.pack(side=LEFT)
l3.pack(side=LEFT)
l2.pack(side=LEFT)
l4.pack(side=LEFT)
fr_top.pack(padx=10,pady=10)
fr_bot.pack()
root.mainloop()
#grid(row=0,colum=0),place