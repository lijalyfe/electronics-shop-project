import csv
import os

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
        self._name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)


    def __repr__(self):
        return f"Item('{self._name}', {self.price}, {self.quantity})"


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self._name = value
        else:
            raise ValueError("Длина наименования товара превышает 10 символов.")

    @staticmethod
    def string_to_number(s):
        return float(s.strip())

    @classmethod
    def instantiate_from_csv(cls):
        current_dir = os.path.dirname(__file__)
        filename = os.path.abspath(os.path.join(current_dir, "items.csv"))
        with open(filename, newline='', encoding='windows-1251') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = int(row['quantity'])
                item = cls(name, price, quantity)
        return cls.all


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
        return None

all_names = [item.name for item in Item.all]
unique_names = set(all_names)
assert len(all_names) == len(unique_names), "Найден дубликат товара"
