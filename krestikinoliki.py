import random
def displayboard(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-+-+-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-+-+-')
    print(board[1]+'|'+board[2]+'|'+board[3])


def proverka():
    while True:
        pr = input('x или o на англ раскладке.').upper()
        if pr == 'X' or 'O':
            break
    if pr == 'X':
        return ['X','O']
    else:
        return ['O','X']


def whoGoesFirst():
    if random.randint(0,1)==0:
        return 'компьютер'
    else:
        return 'человек'


def hod(board,pr,move):
    board[move] = pr





def proverka2(board,pr):
    return((board[1]==pr and board[2]==pr and board[3]==pr) or 
    (board[4]==pr and board[5]==pr and board[6]==pr) or
    (board[7]==pr and board[8]==pr and board[9]==pr) or 
    (board[7]==pr and board[4]==pr and board[1]==pr) or 
    (board[8]==pr and board[5]==pr and board[2]==pr) or 
    (board[9]==pr and board[6]==pr and board[3]==pr) or 
    (board[9]==pr and board[5]==pr and board[1]==pr) or 
    (board[7]==pr and board[5]==pr and board[3]==pr))
    





def board2(x):
    x = []
    for i in board:
        x.append(i)
    return x

def isF(board, move):
    return board[move] == ' '

def proverka3(board):
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isF(board, int(move)):
        print('Ваш следующий ход? Введите номер ячейки. (1-9)')
        move = input()
    return int(move)
        

def ai(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isF(board,i):
          possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
ml = [1,3,7,9]

def GKM(board,computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1,10):
        boardCopi = board2(board)
        if isF(board,i):
            hod(boardCopi,computerLetter,i)
            if proverka2(boardCopi,computerLetter):
                return i

    for i in range(1,10):
        boardCopi = board2(board)
        if isF(board,i):
            hod(boardCopi,playerLetter,i)
            if proverka2(boardCopi,playerLetter):
                return i

def isbf(board):
    for i in range(1,10):
        if isF(board, i):
            return False
        return True


print('ИГРА "КРЕСТИКИ-НОЛИКИ"')

while True:
    theboard = [' ']*10
    playerLetter,computerLetter = proverka()

    turn = whoGoesFirst()
    print(''+turn+'ходит первым')

    gemeIP = True
    
    while gemeIP:
        if turn == 'человек':
            displayboard(theboard)
            move = proverka3(theboard)
            hod(theboard,playerLetter,move)

            if proverka2(theboard,playerLetter):
                displayboard(theboard)
                print('Поздравляю, ты выиграл')
                gameIP = False
            else:
                if isbf(theboard):
                    displayboard(theboard)
                    print('Ничья!')
                    break
                else:
                    turn = 'компьютер'

        else:
            move = GKM(theboard,computerLetter)
            hod(theboard,computerLetter,move)
            if proverka2(theboard,computerLetter):
                displayboard(theboard)
                print('Вы пршогиграли')
                gameIP = False
            else:
                if isbf(theboard):
                    displayboard(theboard)
                    print('Ничья!')
                    break
                else:
                    turn = 'человек'
    print('Еще раз')
    if not input().lower().startswith('д'):
        break
