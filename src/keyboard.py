from src.item import Item


class LanguageMixin:
    """Миксин класса для хранения и изменения языка"""
    LANGUAGES = ["EN", "RU"]
    language = "EN"

    def change_lang(self):
        """Метод для изменения языка."""
        if self.language == "EN":
            self.language = "RU"
        else:
            self.language = "EN"


class Keyboard(Item, LanguageMixin):
    """Класс для товара "Клавиатура" """
    def __init__(self, name, price, quantity, language="EN"):
        super().__init__(name, price, quantity)
        self.set_language(language)

    def set_language(self, language):
        """Устанавливает язык клавиатуры."""
        if language not in self.LANGUAGES:
            raise ValueError("Language not supported")
        self.language = language

    def __str__(self):
        return super().__str__()
