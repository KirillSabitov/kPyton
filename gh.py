
import random


KOL_CIFR=3
KOL_POP=10

def generator_Cisla():
    numbers = list(range(10))
    random.shuffle(numbers)
    secretnum = ''
    for i in range(KOL_CIFR):
        secretnum += str(numbers[i])
    return secretnum

def podskazka(chislogames,chislocom):
    if chislogames == chislocom:
        return 'Вы угадали!'

    podskazka = []
    for i in range(len(chislogames)):
        if chislogames[i] == chislocom[i]:
            podskazka.append('Горячо')
        elif chislogames[i] in chislocom:
            podskazka.append('Тепло')

    if len(podskazka)==0:
        return 'Холодно'


    podskazka.sort()
    return ' '.join(podskazka)

def provvoda(num):
    
    if num == '':
        return False
    

   
    for i in num:
        
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():

            return False
    return True

def playAgain():
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


#осноное тело
print('Я загадаю %s-х значное число, которое вы должны отгадать' %(KOL_CIFR))
print('Я дам несколько подсказок...')
print('Если я говорю:           Это значит:')
print('   Горячо                Отгадана цифра и ее позиция')
print('   Тепло                 Отгадана цифра но не ее позиция')
print('   Холодно               Не отгадана ни одна цифра')


while True:
    secretnum = generator_Cisla()

    print('У вас есть %s попыток, чтобы отгадать число' %KOL_POP)
    popytka = 1
    while popytka <= KOL_POP:
        chislogames=''
        while len(chislogames) != KOL_CIFR or not provvoda(chislogames):
            print('Попытка № %s:' % (popytka))
            chislogames = input()

        print(podskazka(chislogames,secretnum))

        popytka += 1

        if chislogames == secretnum:
            break
        if popytka > KOL_POP:
            print('Попыток больше не осталосью я загадал число %s/' % (secretnum))

    if not playAgain():
        break