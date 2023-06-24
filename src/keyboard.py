from src.item import Item


class LanguageMixin:
    """Миксин класса для хранения и изменения языка"""
    LANGUAGES = ['EN','RU']
    def __init__(self):
        self.__language = "EN"


    @property
    def language(self):
        return self.__language


    @language.setter
    def language(self, lang):
        if lang not in self.LANGUAGES:
            raise ValueError("Недопустимый язык")
        self.__language = lang



    def change_lang(self):
        """Метод для изменения языка."""
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"

class Keyboard(Item, LanguageMixin):
    """Класс для товара "Клавиатура" """
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def __str__(self):
        return super().__str__()