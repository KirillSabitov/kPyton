print('Введите число')
v = input()
while not v.isnumeric():
    print('Вы должны были ввести только цифры')
    v = input()
v = int(v)