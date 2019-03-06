n = int(input('Введите длину списка: '))
dict = []
count = 0
for i in range(0, n):
    dict.append(int(input('Введите ' + str(i) + ' элемент списка: ')))
print(dict)
dict = [x for x in dict if x % 2 != 0]
for i in range(2):
    dict.append(int(input('Введите новый элемент: ')))
print(dict)