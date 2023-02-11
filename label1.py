from tkinter import *
 
 
def take():
    lab['text'] = "Выдано"
 
 
root = Tk()
 
Label(text="Пункт выдачи",fg='#ff0000').pack()

Button(text="Взять",fg='blue', command=take).pack()
 
lab = Label(width=10, height=1,bg='#ff0000')
lab.pack()
 
root.mainloop()