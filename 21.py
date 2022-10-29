import random

def displayboard():
    board = ['''
+-------+
|       |
|       |
|       |
+-------+''','''
+-------+
|       |
|   *   |
|       |
+-------+''','''
+-------+
|*      |
|       |
|      *|
+-------+''','''
+-------+
|*      |
|   *   |
|      *|
+-------+''','''
+-------+
|*     *|
|       |
|*     *|
+-------+''','''
+-------+
|*     *|
|   *   |
|*     *|
+-------+''','''
+-------+
|*     *|
|*     *|
|*     *|
+-------+'''
]
    return board


def pravila():
    print('Игра 21 очко.')
    print('Вы хотите прочитать правила?')
    while True:
        otvet = input().lower()
        if  (otvet =='да') or (otvet =='д') or (otvet =='yes') or (otvet =='y'):
            print('''Вы кидаете игральные кости, пока не наберут общую сумму:21 или приблизительно 21 очко.
Если игрок набрал больше 21 очка, то все баллы аннулируются и игрок проигрывает. 
Вы можете остановиться и не рисковать, передав ход компьютеру, он будет пытаться перебить ваш счет.''')
            a = input('Нажмите enter для продолжения')
            return True
        elif (otvet =='нет') or (otvet =='н') or (otvet =='no') or (otvet =='n'):
            return False
        else:
            print('''Я вас не понял.
Введите ответ еще раз.''')


def getrandomcislo():
    kubik1 = random.randint(1,6)
    kubik2 = random.randint(1,6)
    kub =[]
    kub.append(kubik1)
    kub.append(kubik2)
    return kub


def playAgen():
    print('Хотите сыграть еще раз?')
    while True:
        otvet = input().lower()
        if  (otvet =='да') or (otvet =='д') or (otvet =='yes') or (otvet =='y'):
            return True  

        elif (otvet =='нет') or (otvet =='н') or (otvet =='no') or (otvet =='n'):
            return False

        else:
            print('''Я вас не понял.
Введите ответ еще раз.
Введите "да" для продолжения и "нет" для завершения.''')


def display(gamer,board,kubik1,kubik2,balk,balg):
    print(gamer)
    print()
    print(board[kubik1])
    print(board[kubik2])
    print()
    print('''Количество очков:
    компьютер:'''+str(balk)+'''
    Вы:'''+str(balg))
    




pravila()
ktobrosaet = 'Человек'
kub = displayboard()
balk = 0
balg = 0
game = True
gamer = True
computer = True

while game:
    while gamer:
        kubik1,kubik2 = getrandomcislo()
        balg = balg + kubik1 + kubik2
        display(ktobrosaet,kub,kubik1,kubik2,balk,balg)
        if balg > 21:
            print('Вы проиграли!')
            game = False
            gamer = False
            computer = False
        if game and not (input('(б)росаем еще или (п)ередаем ход?').upper()=='Б'):
            gamer = False
    while computer:
        kubik1,kubik2 = getrandomcislo()
        balk = balk + kubik1 + kubik2
        display(ktobrosaet,kub,kubik1,kubik2,balk,balg)
        if balk > 21:
            print('Вы выиграли!')
            game = False
            computer = False
        elif balk > balg:
            print('Вы проиграли!')
            game = False
            computer = False
        elif balk == balg:
            print('Ничья!')
            game = False
            computer = False
        a = input('Нажмите enter для продолжения')
    if not playAgen():
        break
        

