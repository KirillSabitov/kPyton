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
    print('   '+('1234567890'*6))
    print(strOne)


def getRandomChests(kolChests):
    chests = []
    while len(chests)<=kolChests:
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
        return 'Вы нашли сундук с сокровищами на затонувшем корабле'
    else:
        if mindistanse < 10:
            board[x][y] = str(mindistanse)
            return 'Сундук с сокровищами обнаружен на расстоянии %s единиц от сонара.'% (mindistanse)
        else:
            board[x][y] = 'X'
            return 'Сонар ничего не обнаружил, все сундуки вне пределав досягаемости'




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




# ******************************************************************
# Основное тело
# ******************************************************************
q = [[1,2],[11,7]]
hod = enterplayermove(q)
print(hod)