"""
Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном
товаре. В кортеже должно быть два элемента
— номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество,
единица измерения). Структуру нужно сформировать
программно, т.е. запрашивать все данные у пользователя.
Cобрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например
название, а значение — список значений-характеристик,
например список названий товаров.
"""
product_template = {
    'название': ("имя товара", str),
    'цена': ('стоимость товара', int),
    'количество': ('количество товара', int),
    'ед': ('единицы измерения (шт, кг, и тд)', str)}
next_enter = True
auto_inc = 1
products_list = []
while next_enter:
    product = {}
    for key, value in product_template.items():
        while True:
            user_value = input(f'{value[0]}\n')
            try:
                user_value = value[1](user_value)
            except ValueError as e:
                print(f"{e}\nНе верное значение данных")
                continue
            product[key] = user_value
            break
    products_list.append((auto_inc, product))
    auto_inc += 1
    while True:
        next_add = input("Добавить еще продукт? Да/Нет\n")
        if next_add.lower() in ('да', 'нет'):
            next_enter = next_add.lower() == 'да'
            break
        else:
            print('Неверный ввод, повторите')
print(products_list)
products_analytics = {}
for key in product_template:
    result = []
    for itm in products_list:
        result.append(itm[1][key])
    products_analytics[key] = result
print(products_analytics)
