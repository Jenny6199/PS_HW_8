""" Author Maksim Sapunov msdir6199@gmail.com 30/01/2021 """

# Задача 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# Задача 5. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
#
# Задача 6. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.


class Warehouse:
    """ Представление склада """

    def __init__(self, size=(10, 10, 3)):
        self.size = size
        self.count_of_boxes = 0
        self.table_of_boxes = []
        self.free_size = size

    def get_box_to_keep(self, el):
        """ Производится добавление коробок на склад """
        self.table_of_boxes.append(el)
        print(f'Коробка с {el.name} принята на склад')
        self.count_of_boxes += 1
        return

    def get_wh_statistic(self):
        """ Выводит информацию о складе на экран """
        decor = '\n' + '*'*30
        print(
            decor,
            f'Размеры склада: {self.free_size}',
            f'В настоящий момент на складе находится {self.count_of_boxes} коробок',
            decor,
            sep='\n')

    def show_list_of_boxes(self):
        """ Выводит информации о технике находящейся на складе"""
        if len(self.table_of_boxes) == 0:
            print('В настоящий момент склад пуст.')
        else:
            print('На хранении находятся:\n')
            for el in self.table_of_boxes:
                print(f'Статус: --на складе-- ', el.name)
        return

    def count_technic(self):
        """ Подсчет количества объектов на складе с указанным параметром"""
        result = {
            'printer': 0,
            'scanner': 0,
            'xerox': 0}

        for el in self.table_of_boxes:
            if type(el) == Printer:
                result['printer'] += 1
            elif type(el) == Xerox:
                result['xerox'] += 1
            elif type(el) == Scanner:
                result['scanner'] += 1
        return result


class OfficeTechnic:
    """ Общее представление офисной техники """

    number_of_technic = 0
    type_of_technic = ['printer', 'xerox', 'scanner']

    """ Общее представление техники """

    def __init__(self, name='unnamed_technic'):
        OfficeTechnic.number_of_technic += 1
        self.name = name + '_' + str(OfficeTechnic.number_of_technic)
        self.size = BoxSize()

    @staticmethod
    def create_new_technic(class_of_technic: str):
        """ Создает новый объект техники """
        if class_of_technic.lower() in OfficeTechnic.type_of_technic:
            if class_of_technic.lower() == 'printer':
                return Printer()
            elif class_of_technic.lower() == 'xerox':
                return Xerox()
            elif class_of_technic.lower() == 'scanner':
                return Scanner()
        else:
            print('Данный вид техники недоступен. Посмотрите список доступной техники :')
            print(OfficeTechnic.type_of_technic)
            return OfficeTechnic()


class Printer(OfficeTechnic):
    """ Представление принтера """

    _serial_number = 0

    def __init__(self, name='printer'):
        """ Инициализирует создание объекта класса принтер"""
        OfficeTechnic.__init__(self, name)
        self.serial_number = Printer._serial_number + 1
        self.speed_of_print = 10


class Xerox(OfficeTechnic):
    """ Представление ксерокса """

    _serial_number = 0

    def __init__(self, name='xerox'):
        OfficeTechnic.__init__(self, name)
        self.serial_number = Xerox._serial_number + 1
        self.pixel = (1200, 600)


class Scanner(OfficeTechnic):
    """ Представление сканера """

    _serial_number = 0

    def __init__(self, name='scanner'):
        OfficeTechnic.__init__(self, name)
        self.dpi = 1600


class BoxSize:
    """ Создает атрибуты и методы определяющие размеры упаковки """

    def __init__(self, length=0.45, width=0.45, high=0.4):
        self.length = length  # Длина объекта
        self.width = width  # Ширина объекта
        self.high = high  # Высота объекта
        self.sizes = (length, width, high)

    def set_packed_size(self):
        """ Устанавливает размеры предмета после распаковки"""
        pass


class Office:
    """ общее представление офиса """

    own_technic = []

    @staticmethod
    def new_technic_input():
        """ Функция создает список имеющихся объектов офисной техники"""
        i = 'y'
        while i == 'y':
            print('Ввод имеющихся образцов техники:\n')
            technic = input('Введите тип устройства: ')
            Office.own_technic.append(OfficeTechnic.create_new_technic(technic))
            print(f'Добавлено - {technic}')
            i = input('Вы хотите продолжить ввод? y/n ')
        return

    def show_all_technic(self):
        """ Функция выводит на экран список техники находящейся в офисе"""
        if len(self.own_technic) == 0:
            print('В настоящий момент в офисе нет техники.')
        else:
            for el in self.own_technic:
                print('Статус: --в офисе-- ', el.name)


def menu(my_warehouse: Warehouse, my_office: Office):
    """ Обеспечивает интерактивное меню для управления движением техники со склада в офис и обратно """
    decor = ' '*15
    while True:
        print('Что Вы хотели предпринять?')
        print(decor + 'Ввести новый элемент имеющейся техники --> 1',
              decor + 'Показать список техники имеющейся на складе --> 2',
              decor + 'Показать список техники имеющейся в офисе -->3',
              decor + 'Выдать технику со склада в офис --> 4',
              decor + 'Передать технику из офиса на склад --> 5 ',
              decor + 'Выйти из программы --> 6',
              sep='\n')
        choose = (input('Введите цифру соответствующую Вашему выбору: '))
        try:
            choose = int(choose)
        except ValueError:
            print('Ошибка ввода. Выберите из имеющихся значений.')
        if choose == 1:
            my_office.new_technic_input()
        elif choose == 2:
            my_warehouse.show_list_of_boxes()
            print(f' В настоящий момент на складе {my_warehouse.count_technic()}.')
        elif choose == 3:
            my_office.show_all_technic()
        elif choose == 4:
            for el in my_warehouse.table_of_boxes:
                my_office.own_technic.append(el)
                my_warehouse.table_of_boxes.remove(el)
        elif choose == 5:
            for el in my_office.own_technic:
                my_warehouse.get_box_to_keep(el)
                my_office.own_technic.remove(el)
        elif choose == 6:
            break


Wh_1 = Warehouse()  # Создаем склад
Wh_1.get_wh_statistic()

Of_1 = Office()  # Создаем офис

menu(Wh_1, Of_1)  # Передаем объекты склада и офиса в функцию для использования пользователем

Wh_1.get_wh_statistic()  # Отчет на выхоте
Wh_1.show_list_of_boxes()

