# Игра Fizz-Buzz
# Есть детская игра FizzBuzz, где нужно называть числа подряд, соблюдая всего три правила:
# Если число делится на 3, вместо него надо сказать «Fizz».
# Если число делится на 5, вместо него надо сказать «Buzz».
# А если число делится одновременно на 3 и на 5, то надо вместо него сказать «FizzBuzz».
# На вход подается число num, нужно вывести числа или слова по порядку от 1 до num (включительно) согласно правилам игры
def write_list(size: int) -> list[int]:
    # Эта функция создаёт список от 1 до num
    my_list = [i for i in range(1, size + 1)]
    return my_list
def fizz_buzz(list_fiz : list) -> list:
    # Эта функция меняет список согласно правилам игры Fizz-Buzz
    for i in range(len(list_fiz)):
        if list_fiz[i] % 3 == 0 and list_fiz[i] % 5 == 0:
            list_fiz[i] = "FizzBuzz"
        elif list_fiz[i] % 3 == 0:
            list_fiz[i] = "Fizz"
        elif list_fiz[i] % 5 == 0:
            list_fiz[i] = "Buzz"
    return list_fiz

fizz_num = int(input(" Ввидите натуральное число чтобы сыграть в «FizzBuzz»: "))
print(fizz_buzz(write_list(fizz_num)))
