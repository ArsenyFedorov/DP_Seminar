# На вход подается целое число, необходимо поменять местами первую и последняя цифру в числе
num = input("Ввидите целое число:")
num = num.replace("-", "")
my_list = list()
for i in num:
    my_list.append(i)
my_list[0], my_list[-1] = my_list[-1], my_list[0]
print(*my_list)
