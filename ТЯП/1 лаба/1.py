a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
c = int(input('Введите число C: '))
d = int(input('Введите число D: '))
k = int(input('Введите число k: '))
if b != 0 and a != 0:
    print(abs((a**2 - b**3 - c**3 * a**2) * (b - c + c * (k-d/b**3)) - ((k/b - k/a)*c)**2 - 20000))
else:
    print('Переменные A и B не могут равняться нулю, так как на ноль делить нельзя.')
