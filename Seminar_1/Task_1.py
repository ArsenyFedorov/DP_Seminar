# На вход подается число с плавающей точкой, выведите первую цифра дробной части
float_num = input("Ввидите число с плавающей точкой:")
float_num = float_num.replace("-", "")
float_num = float(float_num)
float_num *= 10
float_num = int(float_num)
print(f"Первая цифра после запятой:{float_num% 10}")
