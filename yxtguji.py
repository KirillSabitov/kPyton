import random
HANGMAN = ['''
 +---+
     |
     |
     |
    ===''','''
 +---+
 0   |
     |
     |
    ===''','''
 +---+
 0   |
 |   |
     |
    ===''','''
 +---+
 0   |
/|   |
     |
    ===''','''
 +---+
 0   |
/|\  |
     |
    ===''','''
 +---+
 0   |
/|\  |
/    |
    ===''','''
 +---+
 0   |
/|\  |
/ \   |
    ===''']
def funk(errorB,yesB,sicretS):
    print(HANGMAN[len(errorB)])
    print()
    print('Ошибочные буквы',end=' ')
    for buk in errorB:
        print(buk,end=' ')
    print()
    leter = '_'*len(sicretS)
    for i in range(len(sicretS)):
        if sicretS[i] in yesB:
            leter = leter[:i]+sicretS[i]+leter[i+1:]
    print(leter)
errorB = 'алку'
yesB = 'о'
sicretS = 'ворон'
funk(errorB,yesB,sicretS)


