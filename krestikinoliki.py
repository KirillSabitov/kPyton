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


#def whoGoesFirst():
  #  if random.randint(0,1)==0:


def hod(board,pr,move):
    board[move] = pr

board = ['','','','','','','','','']
#displayboard(board)
#yach = input('Введите число от одного до девяти')


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


hodp = ai(board,ml)
print(hodp)
hod(board,'O',hodp)
displayboard(board)

board[1] = 'X'
board[7] = 'X'
board[9] = 'X'

hodp = ai(board,ml)
print(hodp)
hod(board,'O',hodp)
displayboard(board)

   # print(qwerty([' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']))
#print(proverka())



