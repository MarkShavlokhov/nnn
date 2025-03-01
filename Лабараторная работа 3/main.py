class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str) -> None:
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """Возвращает название книги."""
        return self._name

    @property
    def author(self) -> str:
        """Возвращает автора книги."""
        return self._author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Дочерний класс, представляющий бумажную книгу. """

    def __init__(self, name: str, author: str, pages: int) -> None:
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        """Возвращает количество страниц."""
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def __str__(self) -> str:
        return f"{super().__str__()} Страниц: {self.pages}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """ Дочерний класс, представляющий аудиокнигу. """

    def __init__(self, name: str, author: str, duration: float) -> None:
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        """Возвращает продолжительность аудиокниги."""
        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = float(value)

    def __str__(self) -> str:
        return f"{super().__str__()} Продолжительность: {self.duration} ч."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


if __name__ == "__main__":
    # Создаем объект базового класса
    book = Book(name="1984", author="Джордж Оруэлл")
    print(book)  # Используется метод __str__
    print(repr(book))  # Используется метод __repr__

    # Создаем объект класса PaperBook
    paper_book = PaperBook(name="1984", author="Джордж Оруэлл", pages=328)
    print(paper_book)  # Используется метод __str__
    print(repr(paper_book))  # Используется метод __repr__

    # Создаем объект класса AudioBook
    audio_book = AudioBook(name="1984", author="Джордж Оруэлл", duration=11.5)
    print(audio_book)  # Используется метод __str__
    print(repr(audio_book))  # Используется метод __repr__

    # Попытка установить недопустимое значение для pages
    try:
        paper_book.pages = -10
    except ValueError as e:
        print(e)  # Количество страниц должно быть положительным целым числом.

    # Попытка установить недопустимое значение для duration
    try:
        audio_book.duration = -5.0
    except ValueError as e:
        print(e)  # Продолжительность должна быть положительным числом.