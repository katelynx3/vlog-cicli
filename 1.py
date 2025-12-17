size = 8
for i in range (size):
    if i % 2 == 0:
        for j in range(size):
            if j % 2 == 0:
                print('W', end=' ')
            else:
                print('B', end=' ')
    else:
        for j in range(size):
            if j % 2 == 0:
                print('B', end=' ')
            else:
                print('W', end=' ')
    print()
