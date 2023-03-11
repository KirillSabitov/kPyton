from tkinter import *

new_vvod = True
chislo = 0

def obr_f(set):
    global new_vvod
    global chislo
    znak = '/','*','+','-','C'.split()
    if set in range(znak):
        chislo = e1.get()
        e1.delete()
    else:
        e1.insert(END,set)

root = Tk()
fr = Frame(root)
fr1 = Frame(root)
fr2 = Frame(root)
fr3 = Frame(root)
e1 = Entry()
b1 = Button(fr2,text='1')
b2 = Button(fr2,text='2')
b3 = Button(fr2,text='3')
b4 = Button(fr1,text='4')
b5 = Button(fr1,text='5')
b6 = Button(fr1,text='6')
b7 = Button(fr,text='7')
b8 = Button(fr,text='8')
b9 = Button(fr,text='9')
b0 = Button(fr3,text='0')
bdel = Button(fr,text='/')
bumn = Button(fr1,text='*')
b1plus = Button(fr2,text='+')
b1minus = Button(fr3,text='-')
brav = Button(fr3,text='=')
bc = Button(fr3,text='C')


e1.pack()
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
b4.pack(side=LEFT)
b5.pack(side=LEFT)
b6.pack(side=LEFT)
b7.pack(side=LEFT)
b8.pack(side=LEFT)
b9.pack(side=LEFT)
b0.pack(side=LEFT)
bdel.pack(side=LEFT)
bumn.pack(side=LEFT)
b1plus.pack(side=LEFT)
brav.pack(side=LEFT)
bc.pack(side=LEFT)
b1minus.pack(side=LEFT)
brav.pack(side=LEFT)
fr.pack()
fr1.pack()
fr2.pack()
fr3.pack()



root.mainloop()