import random
def qwerty(board):
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

print(qwerty([' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']))
print(proverka())