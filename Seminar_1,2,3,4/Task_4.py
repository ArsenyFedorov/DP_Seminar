# Принимаем с консоли число и выводим две последовательности Фибоначчи и Негафибоначчи (можно прочитать в wiki что это)
# Пример: Вводим 8
# [-21, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
fib_list = list()
num = int(input("Ввидите натуральное число :"))

if num == 0:
    fib_list.append(0)
    print(fib_list)
else:
    fib_1 = 1
    fib_2 = 2
    fib_list.append(0)
    fib_list.append(1)
    fib_list.insert(0, 1)
    count = 2
    while num + 1 > count:
        fib_list.append(fib_1)
        fib_list.insert(0, -fib_1)
        fib_2, fib_1 = fib_2 + fib_1, fib_2
        # Присваивание значений фибоначи
        count += 1
    print(fib_list)

