"""
Для списка реализовать обмен значений
соседних элементов, т.е. Значениями
обмениваются элементы с индексами 0 и 1,
2 и 3 и т.д. При нечетном количестве элементов
последний сохранить на своем месте. Для
заполнения списка элементов необходимо использовать
функцию input().
"""
user_input = input("Заполните список значениями через запятую:")
user_list = user_input.split(",")
print(user_list)
index = 0
while index < (len(user_list) - 1):
    user_list[index], user_list[index + 1] = user_list[index + 1], user_list[index]
    index += 2
print(user_list)


