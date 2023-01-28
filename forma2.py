from tkinter import *
from tkinter import ttk

click = 0
window = Tk()
window.title('Кнопка')
window.geometry('800x600')
canvas = Canvas(window, width = 800, height=600,background='white')
def click_button():
    global click
    global canvas
    click +=1 
    btn['text'] = f'{click}'
    canvas = Canvas(window, width = 800, height=600,background='black')
    if click == 5:
        btn['state'] = DISABLED
        btn['text'] = f'Вы выиграли'
        


btn = ttk.Button(text='Нажми 5 раз чтобы выиграть', command=click_button)

btn.pack(side=LEFT)
canvas.pack(expand=True,fill=BOTH)


window.mainloop()