"""
Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя
несколько чисел и строк и сохраните в переменные,
выведите на экран.
"""
name = input("What is your name?\n")
old = int(input("How old are you?\n"))
number = int(input("What is your favourite number?\n"))
happy_number = 3.0
lucky_number = int((old + number) / happy_number)
print("Dear, %s. Your lucky number is %d!" %(name, lucky_number))




