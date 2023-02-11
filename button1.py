from tkinter import *

def cange():
    b1['text'] = 'Изменено'
    b1['bg'] = '#000000'
    b1['activebackground'] = '#555555'
    b1['fg'] = '#ffffff'
    b1['activeforeground'] = '#ffffff'

root = Tk()
b1 = Button(text='Изменить',width=15,height=3)
b1.config(command=cange)
b1.pack()
root.mainloop()