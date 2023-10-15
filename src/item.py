import csv
import os
# file = '../src/items.csv'

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return self.price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name[:10]


    @classmethod
    def instantiate_from_csv(cls, csv_filename):
        """ класс-метод, инициализирующий экземпляры класса Item данными из файла формата ххх.csv"""
        cls.all.clear()
        # Функция os.path.split() разбивает путь на кортеж (голова, хвост), где хвост - последний компонент пути, а голова - всё остальное.
        # Хвост никогда не начинается со слеша (если путь заканчивается слешем, то хвост пустой). Если слешей в пути нет, то пустой будет голова.
        # os.path.dirname(path) - возвращает имя директории пути path.
        # os.path.join(path1[, path2[, ...]]) - соединяет пути с учётом особенностей операционной системы.
        path_file = os.path.join(os.path.dirname(__file__), os.path.split(csv_filename)[1])
        with open(path_file, 'r', encoding='windows-1251', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            items = []
            for row in reader:
                item = cls(row['name'], float(row['price']), int(row['quantity']))
                items.append(item)
            cls.all = items
            return cls.all

    """[{'name': 'Смартфон', 'price': '100', 'quantity': '1'},
     {'name': 'Ноутбук', 'price': '1000', 'quantity': '3'}, 
     {'name': 'Кабель', 'price': '10', 'quantity': '5'}, 
     {'name': 'Мышка', 'price': '50', 'quantity': '5'}, 
     {'name': 'Клавиатура', 'price': '75', 'quantity': '5'}]
     """


    @staticmethod
    def string_to_number(string):
        """ статический метод, возвращающий число из числа-строки
        Для работы с csv-файлом используйте модуль csv метод DictReader"""
        return int(float(string))


