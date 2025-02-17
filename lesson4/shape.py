"""
Напишите класс Shape, представляющий геометрическую фигуру, имеющий следующие методы:

- __init__(self, name): конструктор, принимающий имя геометрической фигуры;
- area(self): метод, который вычисляет площадь геометрической фигуры.

Напишите класс Rectangle, наследующийся от класса Shape, представляющий прямоугольник, имеющий следующие методы:

- __init__(self, name, width, height): конструктор, принимающий имя прямоугольника, ширину и высоту;
- area(self): метод, который вычисляет площадь прямоугольника.

Напишите класс Triangle, наследующийся от класса Shape, представляющий треугольник, имеющий следующие методы:

- __init__(self, name, base, height): конструктор, принимающий имя треугольника, основание и высоту;
- area(self): метод, который вычисляет площадь треугольника.
"""


class Shape:
    """ класс Shape, представляющий геометрическую фигуру """

    def __init__(self, name):
        """ конструктор, принимающий имя геометрической фигуры """
        self.name = name

    def area(self):
        """ метод, который вычисляет площадь геометрической фигуры """
        return "0"

class Rectangle(Shape):
    """ класс Rectangle, наследующийся от класса Shape, представляющий прямоугольник """

    def __init__(self, name, width, height):
        """ конструктор, принимающий имя прямоугольника, ширину и высоту """
        super().__init__(name)
        self.height = height
        self.width = width

    def area(self):
        """ метод, который вычисляет площадь прямоугольника """
        return self.height * self.width

class Triangle(Shape):
    """ класс Triangle, наследующийся от класса Shape, представляющий треугольник """

    def __init__(self, name, base, height):
        """ конструктор, принимающий имя треугольника, основание и высоту """
        super().__init__(name)
        self.height = height
        self.base = base

    def area(self):
        """ метод, который вычисляет площадь треугольника """
        return self.height * (self.base * 2)


shape = Shape("Shape")
print(shape.area())  # 0

rect = Rectangle("Rectangle", 5, 10)
print(rect.area())  # 50

tri = Triangle("Triangle", 6, 4)
print(tri.area())  # 12
