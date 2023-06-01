# Дан список чисел. Создать новый список, который будет содержать только уникальные элементы исходного списка
import random

size = int(input("Ввидите длину списка:"))
my_list = [random.randint(0, 10) for i in range(size)]
print(f"{my_list} -> Список чисел")
print(f"{sorted(list(set(my_list)))} -> Список уникальных чисел")


