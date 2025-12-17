num = input("Введите число ")
num_root = 11
num_root_str = num
while num_root >= 10:
    num_root = 0
    for i in num_root_str:
        num_root += int(i)
    num_root_str = str(num_root)
print(num_root)
