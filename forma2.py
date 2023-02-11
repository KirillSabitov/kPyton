from tkinter import *
from tkinter import ttk

click = 0
window = Tk()
window.title('Кнопка')
window.geometry('800x600')

def click_button():
    global click

    click +=1 
    btn['text'] = f'{click}'    
    if click == 5:
        btn['state'] = DISABLED
        btn['text'] = f'Вы выиграли'
        


btn = ttk.Button(text='Нажми 5 раз чтобы выиграть', command=click_button)

btn.pack(side=LEFT)



window.mainloop()