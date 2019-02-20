import random

number = random.randint(0, 100)
fortune = False
while fortune == False:
    predict = int(input('Введите ваше число: '))
    if predict == number:
        print('Поздравляю! Вы выиграли!')
        fortune = True
    else:
        if predict > number:
            print('Загаданное число меньше!')
        else:
            print('Загаданное число больше!')
