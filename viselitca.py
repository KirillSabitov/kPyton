import random
def sozdanieV():
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
[0   |
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
    return HANGMAN 
#создаем список,
world={'животные':'антилопа барсук медведь бизон кабан мышь бык кот шимпанзе бурундук крокодил корова олень собака осел утка слон хорек лиса лягушка жираф коза заяц хомяк еж бегемот конь обезьяна свинья кролик змея белка тигр волк зебра ворона курица орел гусь носорог баран рысь ласточка крот'.split(),
'фигуры':'шар конус параллелепипед цилиндр пирамида сфера квадрат трапеция параллелограмм ромб треугольник прямоугольник'.split(),
'цвета':'красный оранженвый желтый зеленый голубой синий фиолетовый розовый белый черный серый бежевый коричневый бирюзовый салатовый'.split()}
def getRandomWord(worldlist):
    wordKey = random.choice(list(worldlist.keys()))

    worldIndex = random.randint(0,len(worldlist[wordKey])-1)
    return [worldlist[wordKey][worldIndex],wordKey]

def funk(errorB,yesB,sicretS):
    print(hm[len(errorB)])
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
            return slozhnost()

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

def delVis(vyBs,hangp):
    if vyBs == "с":
        del hangp[10]
        del hangp[9]
    if vyBs == "т":
        del hangp[10]
        del hangp[9]
        del hangp[8]
        del hangp[7]

delV = True
errorB = ''
yesB = ''
gameOver = False
sicretS,keyW = getRandomWord(world)


while True:
    if delV:
        hm = sozdanieV()


        bs = slozhnost()
        delVis(bs,hm)
        delV = False
    
    if bs == 'л':
        print(keyW)

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
        if len(errorB) == len(hm) - 1:
            funk(errorB,yesB,sicretS)
            print('Вы исчерпали все попытки!\nНеугадано букв:'+str(len(errorB))+', и угадано букв:'+str(len(yesB))+'.Было загадано слово:"'+sicretS+'".')
            gameOver = True

    if gameOver:
        if playAgen():
            errorB = ''
            yesB = ''
            gameOver = False
            sicretS,keyW = getRandomWord(world)
            delV = True
        else:
            break