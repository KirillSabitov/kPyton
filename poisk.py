import random
import math
import sys

# ******************************************************************
# Раздел созданых функций
# ******************************************************************



def getplayPole():
    board = []
    for x in range(60):
        board.append([])
        for y in range(15):
            if random.randint(0,1)==0:
                board[x].append('~')
            else:
                board[x].append('`')
    return board

def displayBoard(board):
    strOne = '    '
    for i in range(1,6):
        strOne += ' '*9 + str(i)

    print(strOne)
    print('   '+('1234567890'*6))
    print()

    for stroka in range(15):
        if stroka<10:
            strPol = ' '
        else:
            strPol = ''

        strBoard = ''
        for stolbec in range(60):
            strBoard += board[stolbec][stroka]

        print('%s%s %s %s' % (strPol,stroka,strBoard, stroka))

    print()
    print('   '+('0123456789'*6))
    print(strOne)

def getRandomChests(kolChests):
    chests = []
    while len(chests)<kolChests:
        newchests = [random.randint(0,59),random.randint(0,14)]
        if newchests not in chests:
            chests.append(newchests)
    return chests
    

def vopros(textVoprosa):
    print(textVoprosa)
    while True:
        otvet = input().lower()
        if  (otvet =='да') or (otvet =='д') or (otvet =='yes') or (otvet =='y'):
            # Ответ да запускам игру еще раз
            return True
        elif (otvet =='нет') or (otvet =='н') or (otvet =='no') or (otvet =='n'):
            # Ответ нет завершаем игру
            return False
        else:
            print('''Я вас не понял.''')


def isonboard(x,y):
    return x>=0 and x<=59 and y>=0 and y<=14

def makeMove(board,chests,x,y):
    mindistanse = 100
    for cx,cy in chests:
        distanciya = math.sqrt((cx-x)*(cx-x)+(cy-y)*(cy-y))
        if distanciya < mindistanse:
            mindistanse = distanciya
    mindistanse = round(mindistanse)

    if mindistanse == 0:
        chests.remove([x,y])
        # не потставить ли х на игровое поле
        print( 'Вы нашли сундук с сокровищами на затонувшем корабле')
        return True

    else:
        if mindistanse < 10:
            board[x][y] = str(mindistanse)
            print( 'Сундук с сокровищами обнаружен на расстоянии %s единиц от сонара.'% (mindistanse))
            return  False
        else:
            board[x][y] = 'X'
            print( 'Сонар ничего не обнаружил, все сундуки вне пределов досягаемости')
            return  False

def enterplayermove(predhoda):
    print('''Где следует опустить гидролокатор?
    (координаты: 0-59 0-14)
    (или наберите: "выход" для прекращения игры).''')
    while True:
        move = input()
        if move.lower() == 'выход':
            print('Спасибо за игру!')
            sys.exit()

        move = move.split()

        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isonboard(int(move[0]),int(move[1])):
            if [int(move[0]),int(move[1])] in predhoda:
                print('Вы уже опускали сюда гидролокатор.')
            else:
                return [int(move[0]),int(move[1])]
        else:
            print('Введите число от 0 до 59, потом пробел, а затем число от 0 до 14')

def showinstructag():
    print('''     Инструктаж:
        Вы - капитан корабляб плывущего за сокровищамию Ваша задача - с помощью гидролокатора найти три
        сундука с сокровищами в затонувших судах на дне океана, но гидролокаторы очень просты и определяют
        только расстояние, но не направление.
        Введите координаты, чтобы опустить гидролокатор в воду, на карте будет показано число, обозначающее
        на каком расстоянии находится ближайщий сундук, или будет показана буква Х, обозначающая,
        что сундук в области гидролокатора на обнаружен, на примере карты ниже метки С - это сундуки.
        Цифра три обозначает, что ближайший сундук находится на отдалении в три единицы.
        
                1          2           3
       012345678901234567890123456789012

      0```~~~~``~~`~~~~`~~~``~~~``~`~`~`0
      1`~~~`~`~~~~~`````~````~``~~`~~~~`1
      2`~`C``3`~~~`~`C`~`~```~`~```~~~``2
      3~~~`~`~~~````~`~~~~```~`~`~``~~``3
      4~`~~~`~~~~~``~C~~~~```~~~`````~`~4

       012345678901234567890123456789012
                1          2           3

        (во время игры сундуки на карте не обозначаются)
        Нажмите Enter...
       ''')
    input()
    print('''       Если гидролокатор опущен прямо на сундук, вы можете его поднять, другие гидролокаторы
        обновят данные о расположении ближайшего сундука. Сундуки ниже нахдятся вне диапазона локатора, поэтому
        отображается буква Х.


                 1          2           3
       012345678901234567890123456789012

      0```~~~~``~~`~~~~`~~~``~~~``~`~`~`0
      1`~~~`~`~~~~~`````~````~``~~`~~~~`1
      2`~`X``7`~~~`~`C`~`~```~`~```~~~``2
      3~~~`~`~~~````~`~~~~```~`~`~``~~``3
      4~`~~~`~~~~~``~C~~~~```~~~`````~`~4

       012345678901234567890123456789012
                1          2           3

        (во время игры сундуки на карте не обозначаются)
        Нажмите Enter...
    ''')
    input()
    print('''
        Сундуки с сокровищами не перемещаются. Гидролокаторы определяют сундуки на расстоянии 
        до 9 единиц. Попробуйте поднять все три сундука до того как все гидролокаторы будут опущены в воду.
        
        УДАЧИ!
        
        Нажмите Enter...
        ''')    
    input()

# ******************************************************************
# Основное тело
# ******************************************************************


print('Охотник за сокровищами.')
print()
if vopros('Хотите прочитать иструктаж?'):
    showinstructag()

while True:
    #ДЕЛАЕМ НАСТРОЙКИ ИГРЫ
    #СКОЛЬКО ГИДРОЛОКАТОРОВТ МЫ ДАЕМ ИГРОКУ
    kolgidr = 20
    # игровое поле
    theboard = getplayPole()
    #три сундука
    sunduki = getRandomChests(3)
    # покажем игровое поле
    displayBoard(theboard)
    print()
    # создадим переменную куда будем помещать все ходы игрока
    # это пустой список
    hodygamera = []

    while kolgidr>0:
        # сообщим игроку сколько у него осталосьсвободных гидролокаторов
        # и сколько сундуков надо найти
        if len(sunduki) == 1:
            okon = ''
        else :
            okon = 'a'
        print('Осталось гидролокаторов:%s, осталось %s сундук%s.'% (kolgidr,len(sunduki),okon))
        # примем от игрока координаты куда он хочет опустить гидролокатор
        x,y = enterplayermove(hodygamera)
        # добавим принятые от игрока координаты  в список уже сделаных игроком ходов
        hodygamera.append([x,y])


        if makeMove(theboard,sunduki,x,y):
            # обновить все гидрол
            a = 'ыместо этого будет цикл'
        # показать игровое поле
        displayBoard(theboard)
        # уменьшаем колво сундуков

        print()
        input()