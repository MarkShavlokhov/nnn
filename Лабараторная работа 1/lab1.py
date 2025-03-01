# TODO Написать 3 класса с документацией и аннотацией типов
from abc import ABC, abstractmethod


class Tree(ABC):
    """
    Абстрактный класс, описывающий объект 'Дерево'.
    """

    def __init__(self, height: float, age: int):
        """
        Инициализация атрибутов дерева.

        :param height: Высота дерева в метрах.
        :param age: Возраст дерева в годах.
        """
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом.")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным числом.")

        self.height = height
        self.age = age

    @abstractmethod
    def grow(self, years: int) -> None:
        """
        Увеличивает возраст дерева и его высоту.

        :param years: Количество лет роста дерева.
        """
        ...

    @abstractmethod
    def shed_leaves(self) -> None:
        """
        Описывает процесс сбрасывания листьев.
        """
        ...


class Smartphone(ABC):
    """
    Абстрактный класс, описывающий объект 'Смартфон'.
    """

    def __init__(self, brand: str, storage: int):
        """
        Инициализация атрибутов смартфона.

        :param brand: Бренд смартфона.
        :param storage: Объем памяти устройства в гигабайтах.
        """
        if not brand:
            raise ValueError("Бренд не может быть пустой строкой.")
        if storage <= 0:
            raise ValueError("Объем памяти должен быть положительным числом.")

        self.brand = brand
        self.storage = storage

    @abstractmethod
    def install_app(self, app_size: float) -> None:
        """
        Устанавливает приложение на смартфон.

        :param app_size: Размер приложения в гигабайтах.
        """
        ...

    @abstractmethod
    def take_photo(self, resolution: str) -> None:
        """
        Делает фотографию с указанным разрешением.

        :param resolution: Разрешение фотографии, например '1080p' или '4K'.
        """
        ...


class Vehicle(ABC):
    """
    Абстрактный класс, описывающий объект 'Транспортное средство'.
    """

    def __init__(self, speed: float, fuel_level: float):
        """
        Инициализация атрибутов транспортного средства.

        :param speed: Максимальная скорость транспортного средства в км/ч.
        :param fuel_level: Уровень топлива в литрах.
        """
        if speed <= 0:
            raise ValueError("Скорость должна быть положительным числом.")
        if fuel_level < 0:
            raise ValueError("Уровень топлива не может быть отрицательным.")

        self.speed = speed
        self.fuel_level = fuel_level

    @abstractmethod
    def refuel(self, liters: float) -> None:
        """
        Заправляет транспортное средство топливом.

        :param liters: Количество топлива в литрах.
        """
        ...

    @abstractmethod
    def drive(self, distance: float) -> None:
        """
        Перемещает транспортное средство на заданное расстояние.

        :param distance: Дистанция в километрах.
        """
        ...
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest

    doctest.testmod()
    pass
