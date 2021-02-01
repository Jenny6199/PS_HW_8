""" Author: Maksim Sapunov msdir6199@gmail.com 30/01/2021"""

# Задача 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение
# созданных экземпляров.
# Проверьте корректность полученного результата.

import cmath


class ComplexDigit:
    """ Содержит представление комплексного числа и методы их сложения и умножения"""

    _i = cmath.sqrt(-1)

    def __init__(self, a: int, b: int):
        """ Инициализирует создание объекта класса ComplexDigit"""
        self.a = a
        self.b = b
        self.i = ComplexDigit._i

    def __add__(self, other):
        """ Перегрузка оператора сложения """
        digit = self.a + other.a
        addition = (self.b + other.b)
        print(f'Результат сложения: {digit}+{addition}j')
        return digit, addition * self.i

    def __mul__(self, other):
        """ Перегрузка оператора умножения """
        digit = (self.a * other.a) - (self.b * other.b)
        addition = (self.a * other.b) + (self.b * other.a)
        print(f'Результат умножения: {digit}+{addition}j')
        return digit, addition * self.i

# Вычисления
a = ComplexDigit(5, 3)
b = ComplexDigit(6, 1)
print(a + b)
print(a * b)
# Проверка и сравнение результата вычисления со встроенным методом работы с комплексными числами
x = complex(5, 3)
y = complex(6, 1)
print(x + y)
print(x * y)

