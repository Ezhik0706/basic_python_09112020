"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды
и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
time = int(input("Please, input time in second:" + " "))
hours = time // 3600
minutes = (time % 3600) // 60
seconds = time % 60
print(f"{hours:>02}:{minutes:>02}:{seconds:>02}")
