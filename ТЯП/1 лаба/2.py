import random

number = random.randint(0, 100)
fortune = False
while fortune == False:
    predict = int(input('������� ���� �����: '))
    if predict == number:
        print('����������! �� ��������!')
        fortune = True
    else:
        if predict > number:
            print('��������� ����� ������!')
        else:
            print('��������� ����� ������!')