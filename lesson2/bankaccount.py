"""
Напишите класс BankAccount, имеющий следующие свойства и методы:

- __init__(self, balance): конструктор, принимающий начальный баланс счета
- balance: свойство, которое возвращает текущий баланс счета
- deposit(self, amount): метод, который позволяет внести деньги на счет
- withdraw(self, amount): метод, который позволяет снять деньги со счета
- close(self): метод, который закрывает счет и возвращает оставшиеся на нем деньги

Для свойства balance используйте декоратор @property.
"""


class BankAccount():

    def __init__(self, balance):
        """ конструктор, принимающий начальный баланс счета """
        self.__balance = balance

    @property
    def balance(self) -> int:
        """ свойство, которое возвращает текущий баланс счета """
        return self.__balance

    def deposit(self, amout) -> int:
        """ метод, который позволяет внести деньги на счет """
        self.__balance += amout
        return self.__balance

    def withdraw(self, amout) -> int:
        """ метод, который позволяет снять деньги со счета """
        self.__balance -= amout
        return self.__balance

    def close(self) -> int:
        """ метод, который закрывает счет и возвращает оставшиеся на нем деньги """
        self.__balance -= self.__balance
        return self.__balance



account = BankAccount(1000)
print(account.balance)  # 1000

account.deposit(500)
print(account.balance)  # 1500

account.withdraw(200)
print(account.balance)  # 1300

account.close()
print(account.balance)  # 0
