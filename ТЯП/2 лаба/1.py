string = 'Ли, Литий, Лизергининовый, Лимузин, лицо, литва'
string = string.split(', ')
for i in range(0, len(string)-1):
    if string[i][0] == 'Л' and string[i][1] == 'и':
        print(string[i])