def ex1():
    mass = 2
    volume = 0.5
    name = 'Кирпич'
    density = mass / volume
    print(f'Параметры объекта:\nНазвание объекта: {name}\nМасса: {mass}\nОбъем: {volume}\nПлотность: {density}')
    name = input('Введите новый объект: ')
    mass = int(input('Введите массу: '))
    volume = float(input('Введите объем: '))
    density = mass / volume
    print(f'Параметры нового объекта:\nНазвание объекта: {name}\nМасса: {mass}\nОбъем: {volume}\nПлотность: {density}')


def ex2():
    total_seconds = int(input('Введите количество секунд: '))
    seconds = total_seconds % 60
    minutes = (total_seconds // 60) % 60
    hours = (total_seconds // 3600) % 60
    print('%02i:%02i:%02i' % (hours, minutes, seconds))


def ex3():
    n = int(input('Введите число от 0 до 9: '))
    while n > 9 or n < 0:
        n = int(input('Некорректное число. Введите число от 0 до 9: '))
    print(f'Результат: {n * 100 + n * 10 + n}')


def ex4():
    num = int(input('Введите положительное целое число: '))
    while num % 1 > 0 or num < 0:
        num = int(input('Некорректное число. Введите положительное целое число: '))
    max_digit = 0
    while num > 0:
        if num % 10 > max_digit:
            max_digit = num % 10
        num = num // 10
    print(f'Максимальная цифра в числе равна {max_digit}')


def ex5():
    income = float(input('Введите выручку: '))
    costs = float(input('Введите затраты: '))
    if income > costs:
        print('Фирма отработала с прибылью')
        number_of_emps = int(input('Введите кол-во сотрудников: '))
        profitability = income / costs
        profit_per_emp = (income - costs) / number_of_emps
        print(f'Рентабельность выручки равна {profitability}, прибыль в расчете на сотрудника равна {profit_per_emp}')
    else:
        print('Фирма отработала с убытком')


def ex6():
    distance = float(input('Введите начальную дистанцию: '))
    while distance < 0:
        distance = int(input('Некорректная дистанция. Введите дистанцию еще раз: '))
    end_distance = float(input('Введите конечную дистанцию: '))
    while end_distance < 0:
        end_distance = int(input('Некорректная дистанция. Введите дистанцию еще раз: '))
    count = 0
    while distance <= end_distance:
        distance = distance + distance / 10
        count = count + 1
    print(f'Спортсмен достигнет результата на {count} день')


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
