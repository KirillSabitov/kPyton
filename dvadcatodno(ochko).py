import random

from krestikinoliki import board2
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
            return False
        elif (otvet =='нет') or (otvet =='н') or (otvet =='no') or (otvet =='n'):
            return False
        else:
            print('''Я вас не понял.
Введите ответ еще раз.''')





def game1():
    chislo = random.randint(1,6)
    chislo = displayboard()
    print(chislo)
print(game1())






