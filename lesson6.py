from time import sleep
from datetime import datetime as dt


class TrafficLight:
    """ Класс светофора, реализующий свое переключение при запуске running( """
    _states = {'red': 7, 'yellow': 2, 'green': 10}
    _color = ''

    def running(self):
        """ Метод запусключения светофора """
        for color, sw_time in self._states.items():
            self._color = color
            start_state_time = dt.now()

            print(f"TrafficLight switched to state '{self._color}' "
                  f"on {sw_time} seconds")

            sleep(sw_time)

            print(f"TrafficLight leave state '{self._color}' after" 
                  f"{(dt.now() - start_state_time).seconds} seconds")


def ex1():
    tl = TrafficLight()
    tl.running()


class Road:
    """ Класс дорожного полотна """
    # удельная масса 1кв.м. дорожного полотна толщиной 1 см (тонн)
    _surface_spec_gravity: float = 0.02

    def __init__(self, length: [int, float], width: [int, float]):
        """
        :param length: Длина дорожного полотна в метрах
        :param width: Ширина дорожного полотна в метрах
        """
        self._length = float(length)
        self._width = float(width)

    def get_surface_gravity(self, thickness: float) -> [float, None]:
        """ Рассчет массы дорожного полотна заданной толщина
        :param thickness: Толщина дорожного покрытия в сантиметрах
        :return: Масса дорожного полотна в тоннах если все ОК, иначе None
        """
        try:
            return (self._length * self._width
                    * thickness * self._surface_spec_gravity)
        except TypeError:
            return None


def ex2():
    length = int(input('Введите длину '))
    width = int(input('Введите ширину'))
    thickness = int(input('Введите толщину '))
    try:
        road = Road(length, width)
        print(
            'Масса дорожного покрытия составит:',
            road.get_surface_gravity(thickness),
            'тонн'
        )
    except TypeError:
        print('класс Road требует 2 позиционных аргумента')


class Worker:
    """Класс работника"""

    def __init__(
            self,
            name: str,
            surname: str,
            position: str,
            wage: float = 0,
            bonus: float = 0
    ):
        """
        :param name: Имя работника
        :param surname: Фамилия работника
        :param position: Занимаемая должность
        :param wage: Оклад
        :param bonus: Премия
        """
        self.name = name
        self.surname = surname
        self.position = position

        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    """Класс позиции"""

    def get_full_name(self, reverse=False):
        """ Собирает полное имя для позиции в порядке 'заданном reverse
        :param reverse: порядок следования если False (по умолчанию) 'name surname'
         если True, то 'surname name'
        :return: Полное имя
        """
        return ' '.join(sorted([self.name, self.surname], reverse=reverse))

    def get_total_income(self):
        """ Вычисляет полный доход (оклад + премия)
        :return: Сумма оклада и премии
        """
        return sum(self._income.values())


def ex3():
    position_data = [
        {
            'name': 'Ivan',
            'surname': 'Ivanov',
            'position': 'Scrum master',
            'wage': 40000,
            'bonus': 0
        },
        {
            'name': 'Petr',
            'surname': 'Petrov',
            'position': 'developer',
            'wage': 90000,
            'bonus': 60000
        },
        {
            'name': 'Irina',
            'surname': 'Ivanova',
            'position': 'service delivery manager',
            'wage': 60000,
            'bonus': 30000
        },
    ]

    for item in position_data:
        position = Position(**item)

        print('#######################################')
        print('From data: ', item)
        print('Position name: ', position.name)
        print('Position surname: ', position.surname)
        print('Position full name: ', position.get_full_name())
        print('Position full name reverse: ', position.get_full_name(reverse=True))
        print('Position position: ', position.position)
        print('Position total income: ', position.get_total_income())
        print('#######################################\n\n')


class Car:
    """ Базовый класс автомобиля """
    def __init__(
            self,
            color: str,
            name: str,
            is_police: bool = False
    ):
        """
        :param color: Цвет авто
        :param name: Модель (название) авто
        :param is_police: Признак полицейности
        """
        self.color = color
        self.name = name
        self.is_police = True if is_police else False

        self.speed = 0
        self._direction = ''

    def go(self, speed: float):
        """ Начинает движение авто с заданной скоростью
        :param speed: Скорость движения
        """
        try:
            self.speed = float(speed)
        except ValueError:
            pass

    def stop(self):
        """ Останавливает авто """
        self.speed = 0

    def turn(self, direction: str):
        """ Задает поворот авто в движении
        :param direction: направление поворота ('left', 'right')
        """
        if direction not in ('left', 'right'):
            print(f"'{direction}' invalid direction")
            return

        if not self.speed:
            print(f"'Can't turn to {direction}' in place")
            return

        self._direction = direction

    def show_speed(self):
        """ Показать текущуую скорость """
        print(f'My speed is {self.speed} km/h')

        if (hasattr(self, '_max_granted_speed')
                and self._max_granted_speed
                and self.speed > self._max_granted_speed):
            print(f'Over speed on {self.speed - self._max_granted_speed} km/h')

    @property
    def direction(self):
        """ Показать текущее направление """
        return self._direction


class TownCar(Car):
    """ Класс городских автомобилей """
    # максимальная скорость движения
    _max_granted_speed = 60


class SportCar(Car):
    """ Класс спортивный автомобилей """
    pass


class WorkCar(Car):
    """ Класс авто для работы """
    # максимальная скорость движения
    _max_granted_speed = 40


class PoliceCar(Car):
    """ Класс полицейского авто """
    def __init__(self, *args):
        """
        :param args: Параметры авто
        """
        super().__init__(*args, is_police=True)


def ex4():
    cars_data = {
        ('Yellow', 'Aston Martin Cygnet'): TownCar,
        ('Green', 'BMW M3'): SportCar,
        ('White', 'VAZ 2106'): WorkCar,
        ('Red', 'Ford Crown Victoria'): PoliceCar,
    }

    for car_descr, car_cls in cars_data.items():
        car = car_cls(*car_descr)

        print('#######################################')
        print(f"Car name '{car.name}'")
        print(f"Car color '{car.color}'")
        print(f"Car is police '{car.is_police}'")
        print(f"Car speed '{car.speed}'")
        print(f"Car direction '{car.direction}'")
        print(f"Car show speed '{car.show_speed()}'")

        car.turn('asd')
        car.turn('left')
        car.go('asd')
        print("Car speed after invalid go", car.speed)
        car.go(30)
        car.show_speed()
        car.go(45)
        car.show_speed()
        car.go(75)
        car.show_speed()
        car.turn('left')
        print(f"Car direction '{car.direction}'")
        car.turn('right')
        print(f"Car direction '{car.direction}'")
        car.stop()
        car.show_speed()
        print('#######################################\n\n')


class Stationery:
    title: str

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    title = "ручка"

    def draw(self):
        print(f"{self.title} пишет")


class Pencil(Stationery):
    title = "карандаш"

    def draw(self):
        print(f"{self.title} чертит")


class Handle(Stationery):
    title = "маркер"

    def draw(self):
        print(f"{self.title} рисует")


def ex5():
    stationery = Stationery()
    stationery.draw()

    pen = Pen()
    pen.draw()

    pencil = Pencil()
    pencil.draw()

    handle = Handle()
    handle.draw()


ex_num = int(input('Введите номер задания (1-5), для выхода введите 0'))
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
    ex_num = int(input('Введите номер задания (1-5), для выхода введите 0'))
