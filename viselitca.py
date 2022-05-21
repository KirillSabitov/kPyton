from ast import Index
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
/ \  |
    ===''','''
 +---+
 0   |
/|\  |
/ \  |
    ===''','''
 +---+
[0]  |
/|\  |
/ \  |
    ===''','''
 +---+
 [0] |
[/|\ |
 / \ |
    ===''','''
 +---+
 [0]  |
[/|\] |
 / \  |
     ===''']
#создаем список,
world=['антилопа', 'барсук', 'медведь', 'бизон', 'кабан', 'мышь', 'бык', 'кот', 'шимпанзе', 'бурундук','крокодил', 'корова', 'олень', 'собака', 'осел', 'утка', 'слон', 'хорек', 'лиса', 'лягушка', 'жираф', 'коза', 'заяц', 'хомяк', 'еж', 'бегемот', 'конь', 'обезьяна', 'свинья','кролик', 'змея', 'белка', 'тигр', 'волк', 'зебра', 'ворона', 'курица', 'орел', 'гусь', 'носорог', 'баран', 'рысь', 'ласточка', 'крот']
def getRandomWord(worldlist):
    worldIndex = random.randint(0,len(worldlist)-1)
    return worldlist[worldIndex]

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

def getGuess(alreadyGuessed):
    while True:
        print('Введите букву')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Введите только одну букву')
        elif guess in alreadyGuessed:
            print('Вы уже назвали эту букву')
        elif guess not in 'абвгдежзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста введите букву')
        else:
            return guess


#спрашиваем игрока хочет ли он сыграть еще раз
def playAgen():
    print('Хотите сыграть еще раз?')
    while True:
        otvet = input().lower()
        if  (otvet =='да') or (otvet =='д') or (otvet =='yes') or (otvet =='y'):
            return True

        elif (otvet =='нет') or (otvet =='н') or (otvet =='no') or (otvet =='n'):
            return False
#
        else:
            print('''Я вас не понял.
Введите ответ еще раз.
Введите "да" для продолжения и "нет" для завершения.''')

def slozhnost():
    print('''Выберите уровень сложности.
"Л"для легкого
"C"для среднего
"T"для тяжелого''')
    while True:
        slOtv = input().lower()
        if len(slOtv) != 1:
            print('Введите только одну букву')
        elif slOtv not in 'лст':
            print('"Л"для легкого"C"для среднего"T"для тяжелого')
        else:
            return slOtv

bs = slozhnost()
if bs == "с":
    del HANGMAN[10]
    del HANGMAN[9]
if bs == "т":
    del HANGMAN[10]
    del HANGMAN[9]
    del HANGMAN[8]
    del HANGMAN[7]

errorB = ''
yesB = ''
gameOver = False
sicretS = getRandomWord(world)

while True:
    funk(errorB,yesB,sicretS)

    bukva = getGuess(errorB+yesB)

    if bukva in sicretS:
        yesB = yesB + bukva


        ssYes = True
        for i in range(len(sicretS)):
            if sicretS[i] not in yesB:
                ssYes = False
                break

        if ssYes:
            print('Да! Секретное слово - "'+sicretS+'"! Вы угадали!')
            gameOver = True
    else:
        errorB = errorB + bukva
        if len(errorB) == len(HANGMAN) - 1:
            funk(errorB,yesB,sicretS)
            print('Вы исчерпали все попытки!\nНеугадано букв:'+str(len(errorB))+', и угадано букв:'+str(len(yesB))+'.Было загадано слово:"'+sicretS+'".')
            gameOver = True

    if gameOver:
        if playAgen():
            errorB = ''
            yesB = ''
            gameOver = False
            sicretS = getRandomWord(world)
        else:
            break