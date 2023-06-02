# a и b
# выяснить какакое из них больше не используя не единой операции сравнения

a = int(input("Ввидите число:"))
b = int(input("Ввидите второе число:"))
set_1 = {i for i in range(1, a + 1)}
set_2 = {i for i in range(1, b + 1)}
set_3 = set_1.union(set_2)
set_3 = sorted(list(set_3))
print(f"Число {set_3[-1]} больше")
