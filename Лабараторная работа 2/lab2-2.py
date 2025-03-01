BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    """
    Класс для представления книги с атрибутами:
    - id: Идентификатор книги.
    - name: Название книги.
    - pages: Количество страниц.
    """

    def __init__(self, id_: int, name: str, pages: int):
        """
        Конструктор инициализирует атрибуты книги.

        :param id_: Идентификатор книги.
        :param name: Название книги.
        :param pages: Количество страниц.
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Возвращает строковое представление книги.

        :return: Строка в формате 'Книга "название_книги"'
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Возвращает строку, по которой можно создать аналогичный экземпляр книги.

        :return: Валидная строка для создания экземпляра Book.
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"

# TODO написать класс Library
class Library:
    """
    Класс для представления библиотеки с атрибутами:
    - books: Список книг.
    """

    def __init__(self, books=None):
        """
        Конструктор инициализирует атрибуты библиотеки.

        :param books: Необязательный список книг. По умолчанию пустой список.
        """
        self.books = books if books is not None else []

    def get_next_book_id(self) -> int:
        """
        Возвращает следующий идентификатор для добавления новой книги.

        :return: Идентификатор новой книги.
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги в списке по ее идентификатору.

        :param book_id: Идентификатор книги.
        :return: Индекс книги в списке.
        :raises ValueError: Если книга с таким идентификатором не существует.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
