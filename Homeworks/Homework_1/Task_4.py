"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
number = int(input("Введите целое положительное число:" + " "))
max = number % 10
while number > 0:
    last_digit = number % 10
    number //=10
    if last_digit > max:
        max = last_digit
print(max)
