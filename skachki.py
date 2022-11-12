
def histori():
    print('Вы приходите на ипподром поставить на лошадь.')
    minstavka = input('Минимальная сумма ставки:')
    while not minstavka.isnumeric():
        print('Вы должны были ввести только цифры')
        minstavka = input()
    ncap = input('У вас есть(введите сумму):')
    while not ncap.isnumeric():
        print('Вы должны были ввести только цифры')
        ncap = input()
    while True:
        if minstavka > ncap:
            print('Минимальная ставка не может быть больше вашего изначального капитала.')
            return True
print(histori())