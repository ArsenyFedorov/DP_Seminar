# Проверка на палиндром:
#   а. слова
#   б. предложения

my_str = input("Ввидите слово или предложение:")
my_str = my_str.replace(" ", "")
my_str = my_str.lower()
if my_str == my_str[::-1]:
    print("Yes")
else:
    print("No")

