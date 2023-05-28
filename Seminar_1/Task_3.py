# На вход поступает число: найти сумму цифр числа, в том числе если оно отрицательное или вещественное
num = input("Ввидите число:")
sum_num = 0
num = num.replace(",", "")
num = num.replace(".", "")
num = num.replace("-", "")

if num.isdigit():
    num = int(num)
    while num > 0:
        sum_num += num % 10
        num //= 10
    print(f"Сумма чисел равна:{sum_num}")
else:
    print("Ты походу перепутал ")

