# На вход поступает десятичное число, вывести его в виде двоичного
number = int(input('Введите число:\n'))
print(bin(number))

binary = []
while number > 0:
    binary.append(number % 2)
    number //= 2
binary.reverse()

for i in binary:
    print(i, end='')