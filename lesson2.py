def ex1():
    count = 1
    start_list = [1, 12.5, 'строка', [34, 56]]
    for i in start_list:
        print(f'Номер элемента в списке: {count}, тип данных: {type(i)}')
        count += 1


def ex2():
    start_list = []
    element = input('Введите новый элемент списка, для перестановки элементов введиле "convert" ')
    while element != 'convert':
        start_list.append(element)
        element = input('Введите новый элемент списка, для перестановки элементов введиле "convert" ')
    length = len(start_list)
    i = 0
    while i < length // 2:
        tmp = start_list.pop(i * 2)
        start_list.insert(i * 2 + 1, tmp)
        i += 1
    for i in start_list:
        print(f'{i}')


def ex3():
    months_list = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
    months_dict = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень', 10: 'Осень', 11: 'Осень', 12: 'Зима'}
    num = int(input('Введите номер месяца: '))
    while num < 1 or num > 12:
        num = int(input('Некорректный номер месяца, он должен быть от 1 до 12. Введите номер месяца: '))
    print(f'Данные из списка: в этом месяце - {months_list[num-1]}')
    print(f'Данные из словаря: в этом месяце - {months_dict.get(num)}')


def ex4():
    string = input('Введите строку с пробелами между словами: ')
    start_list = string.split()
    for ind, el in enumerate(start_list):
        print(f'{ind}: {el[0:10]}')


def ex5():
    rating_list = [7, 5, 3, 3, 2]
    new_rating = int(input('Введите новый рейтинг: '))
    count = 0
    for ind, el in enumerate(rating_list):
        if new_rating > el:
            rating_list.insert(ind, new_rating)
            break
        count += 1
    if count == len(rating_list):
        rating_list.append(new_rating)
    print(rating_list)


def ex6():
    final_list = []
    count = 0
    print('Для выхода введите вместо характеристик слово "end"')
    while True:
        input_string = input('Введите через пробел характеристики товара: название, цена, количество, единица измерения\n')
        if input_string == 'end':
            break
        input_list = input_string.split()
        while len(input_list) != 4:
            print('Некорректное количество характеристик')
            input_string = input(
                'Введите через пробел характеристики товара: название, цена, количество, единица измерения\n')
            input_list = input_string.split()
        count += 1
        dictionary = {'Название': input_list[0], 'Цена': input_list[1], 'Количество': input_list[2], 'Единица измерения': input_list[3]}
        cortage = (count, dictionary)
        final_list.append(cortage)
        for el in final_list:
            print(f'{el}\n')


ex_num = int(input('Введите номер задания (1-6), для выхода введите 0'))
while ex_num != 0:
    if ex_num == 1:
        ex1()
    if ex_num == 2:
        ex2()
    if ex_num == 3:
        ex3()
    if ex_num == 4:
        ex4()
    if ex_num == 5:
        ex5()
    if ex_num == 6:
        ex6()
    ex_num = int(input('Введите номер задания (1-6), для выхода введите 0'))
