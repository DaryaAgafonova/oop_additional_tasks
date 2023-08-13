"""
Создай класс `Number` c полем `value` (указывается при инициализации)

Создай экземпляр, например `x = Number(7)`

Добавь методы:

`.get()` возвращает текущее value

`.add(<значение>)` добавляет указанное число к value

`.substract(<значение>)` вычитает указанное число из value
"""

class Number:

    def __init__(self, value):
        """ инициализация атрибутов класса """
        self.value = value

    def get(self):
        """ возвращает текущее value """
        return self.value

    def add(self, meaning):
        """ добавляет указанное число к value """
        self.meaning = meaning
        self.value += self.meaning
        return self.value


    def substract(self, meaning):
        """ вычитает указанное число из value """
        self.meaning = meaning
        self.value -= self.meaning
        return self.value


n = Number(7)
print(n.get())  # 7
n.add(3)
print(n.get())  # 10
n.substract(5)
print(n.get())  # 5
