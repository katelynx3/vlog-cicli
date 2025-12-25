num_1 = int(input('Введите первое число '))
num_2 = int(input('Введите второе число '))
for i in range(num_1, num_2 + 1):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False

    if flag == True:
        print(i)
