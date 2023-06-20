from src.item import Item

class Keyboard(Item, LanguageMixin):
    """Класс для товара "Клавиатура" """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class LanguageMixin:
    """Миксин класса для хранения и изменения языка"""
    LANGUAGES = ['EN','RU']
    def __init__(self, language = 'EN', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._language = language


    @property
    def language(self):
        return self._language


    @language.setter
    def language(self, value):
        if value in self.LANGUAGES
            self._language = value
        else:
            raise ValueError("Недопустимый язык")



