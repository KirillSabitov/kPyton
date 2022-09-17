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


def proverka(board,pr):
    return((board[1]==pr and board[2]==pr and board[3]==pr) or 
    (board[4]==pr and board[5]==pr and board[6]==pr) or
    (board[7]==pr and board[8]==pr and board[9]==pr) or 
    (board[7]==pr and board[4]==pr and board[1]==pr) or 
    (board[8]==pr and board[5]==pr and board[2]==pr) or 
    (board[9]==pr and board[6]==pr and board[3]==pr) or 
    (board[9]==pr and board[5]==pr and board[1]==pr) or 
    (board[7]==pr and board[5]==pr and board[3]==pr))
    


board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
displayboard(board)
print(proverka(board,'X'))
board[3] = 'X'
board[5] = 'X'
board[7] = 'X'
displayboard(board)
print(proverka(board,'X'))



















   # print(qwerty([' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']))
#print(proverka())



