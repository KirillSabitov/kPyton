import random



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
    


# ******************************************************************
# Основное тело
# ******************************************************************


theBoard = getplayPole()
displayBoard(theBoard)
