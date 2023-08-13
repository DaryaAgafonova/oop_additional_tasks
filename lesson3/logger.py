"""
Напишите класс Logger, имеющий следующие методы:

- __init__(self, filename): конструктор, принимающий имя файла, в который будет производиться запись логов;
- __call__(self, message): магический метод, который позволяет использовать объект класса Logger как функцию,
принимающую сообщение и записывающую его в файл.
"""


class Logger:

    def __init__(self, filename=""):
        """ конструктор, принимающий имя файла, в который будет производиться запись логов """
        self.filename = filename

    def __call__(self, message):
        """ магический метод, который позволяет использовать объект класса Logger как функцию,
принимающую сообщение и записывающую его в файл """
        self.message = message
        sms = open(self.filename, "w")
        sms.write(self.message)
        sms.close()


logger = Logger("log.txt")
logger("This is a test message.") # в папке lesson3 создался файл log.txt с текстом This is a test message.
