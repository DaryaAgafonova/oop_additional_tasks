"""
Напишите класс Person, имеющий следующие методы:

- __init__(self, name, age): конструктор, принимающий имя и возраст человека
- display(self): метод, выводящий на экран имя и возраст человека
- from_birth_year(cls, name, birth_year): класс-метод, принимающий имя и год рождения человека и
возвращающий объект класса Person;
- is_adult(cls, age): статический метод, принимающий возраст человека и возвращающий True,
если он старше 18 лет, и False в противном случае
"""
from datetime import datetime

class Person:

    def __init__(self, name, age):
        """ конструктор, принимающий имя и возраст человека """
        self.name = name
        self.age = age

    def display(self):
        """ метод, выводящий на экран имя и возраст человека """
        return f"{self.name.title()} is {self.age} years {self.age}."

    @classmethod
    def from_birth_year(cls, name, birth_year):
        """ класс-метод, принимающий имя и год рождения человека и
возвращающий объект класса Person """
        age_year = datetime.today().year - birth_year
        person_age = cls(name, age_year)
        return person_age

    @staticmethod
    def is_adult(age):
        """ статический метод, принимающий возраст человека и возвращающий True,
если он старше 18 лет, и False в противном случае """
        if age >= 18:
            return True
        else:
            return False


person1 = Person("John", 28)
print(person1.display())  # John is 28 years 28.

person2 = Person.from_birth_year("Mike", 1995)
print(person2.display())  # Mike is 28 years 28.

print(Person.is_adult(20))  # True
print(Person.is_adult(15))  # False
