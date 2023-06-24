from src.item import Item


class LanguageMixin:
    """Миксин класса для хранения и изменения языка"""
    LANGUAGES = ["EN","RU"]
    def __init__(self):
        self._language = "EN"


    @property
    def language(self):
        return self._language


    @language.setter
    def language(self, lang):
        if lang is not None:
            if lang not in self.LANGUAGES:
                raise ValueError("Language not supported")
            self._language = lang



    def change_lang(self):
        """Метод для изменения языка."""
        if self._language == "EN":
            self._language = "RU"
        else:
            self._language = "EN"

class Keyboard(Item, LanguageMixin):
    """Класс для товара "Клавиатура" """
    def __init__(self, name, price, quantity, language=None):
        super().__init__(name, price, quantity)


    def __str__(self):
        return super().__str__()