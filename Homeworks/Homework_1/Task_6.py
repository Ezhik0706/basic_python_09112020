"""
Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 %
относительно предыдущего. Требуется определить
номер дня, на который общий результат спортсмена
составить не менее b километров. Программа должна
принимать значения параметров a и b и выводить одно
натуральное число — номер дня.
"""
a = int(input("Введите какое расстояние пробежал спортсмен в первый день:" + " "))
b = int(input("Введите общий результат спортсмена в км:" + " "))
count_day = 1
result = a
while result <= b:
    result *= 1.1
    count_day +=1
print(f"Результат достигнут на {count_day} день")
