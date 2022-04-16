#"Это игра наперстки"
import random, time

print('Как вас зовут?')
myName = input()

def displayIntro():
    print(myName+''', вы идете по рынку и видите человека, сидящего за столом.
    На столе перед ним находятся три наперстка. Он показывает маленький шарикб который
    накрывает оним из наперстков...''')
    time.sleep(2)
def g():
    print('''После этого он начинает перемещать наперстки все с большей скоростью,
        что даже трудно отследить нужный наперсток''')
    time.sleep(2)
def playGames():

    naperstok = random.randint(1,3)
    print('''Вы решили попытать удачу, отгадав в каком из наперстков назодится шарик!
    Укажите номер наперстка.Введите 1,2 или 3''')
    V = input()
    if naperstok == int(V):
        print('Вы выиграли у незнакомца')

    if naperstok != int(V):
        print('Вы проиграли незнакомцу')
uslovie = input()
while uslovie == 'Y':
    g()
    otvetGamer = g()
    playGames(otvetGamer)
    print('Вы хотите сыграть еще раз?')
    