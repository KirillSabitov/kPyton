import random,time

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
            time.sleep(2)
            print('''Вы кидаете игральные кости, пока не наберут общую сумму:21 или приблизительно 21 очко.
Если игрок набрал больше 21 очка, то все баллы аннулируются и игрок проигрывает. 
Вы можете остановиться и не рисковать, передав ход компьютеру, он будет пытаться перебить ваш счет.''')
            time.sleep(2)
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



def display(board,kubik1,kubik2,balg,balk,gamer):
    print(gamer)
    print(board[kubik1])
    print(board[kubik2])
    print()
    print('''Количество очков:
    компьютер:'''+balk+'''
    Вы:'''+balg)

def hod():
    print('Нажмите б чтобы бросить ')
    while True:
        otvet = input().lower().startswith()
        if otvet == 'б':
            return True
        else:
            print('''Я вас не понял.
Введите ответ еще раз.''')


def vbros():
    print('Вы хотите передать ход?')
    otvet = input().lower()
    if  (otvet =='да') or (otvet =='д') or (otvet =='yes') or (otvet =='y'):
        return True  

    elif (otvet =='нет') or (otvet =='н') or (otvet =='no') or (otvet =='n'):
        return False


#def proverka(balg,balk):
pravila()


    




