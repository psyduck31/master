data = 'Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса;_' \
       'Иванов;Семен;' \
       'Игоревич;22 года;Студент 2 курса;'
data = data.split(';_')
for i in range(0, len(data)-1):
    string = data[i]
    string = string.split(';')
    print(string[0] + ' ' + string[1] + ' ' + string[2] + '       ' + string[3] + '        ' + string[4])