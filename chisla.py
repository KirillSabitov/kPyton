#Это игра по угадыванию чисел
import random

attNumber = 0

print('Привет! Как тебя зовут?')
myName = input()

number = random.randint(1,20)
print('Что ж, '+myName+', я загадываю число от 1 до 20.')

for attNumber in range(6):
   # print('Попробуй угадать') # четыре
    guess = input('Попробуй угадать')
    guess = int(guess)

    if guess < number:
        print('Твое число слишком маленькое') #8

    if guess > number:
        print('Твое число слишком большое.')

    if guess == number:
        break

if guess == number:
    attNumber = str(attNumber + 1)
    print('Отлично, '+myName+' ты справился за '+attNumber+' попытки!')

if guess != number:
    number = str(number)
    print('Увы, я загадал число '+number+'.')
