class Animal:
    def __init__(self, name: str, age: int, species: str) -> None:
        self.name = name
        self.age = age
        self.species = species

    def __str__(self) -> str:
        return f"{self.name} ({self.species}), возраст {self.age} лет"

    def __repr__(self) -> str:
        return f"Animal(name={self.name}, age={self.age}, species={self.species})"

    def make_sound(self) -> str:
        return "Неизвестный звук"


class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str) -> None:
        super().__init__(name, age, species="Собака")
        self.breed = breed

    def __str__(self) -> str:
        return f"{self.name} ({self.breed}), возраст {self.age} лет"

    def __repr__(self) -> str:
        return f"Dog(name={self.name}, age={self.age}, breed={self.breed})"

    def make_sound(self) -> str:
        return "Гав-гав!"

    def fetch(self, item: str) -> str:
        return f"{self.name} принес(ла) {item}!"

if __name__ == "__main__":
    # Создаем объект базового класса
    animal = Animal(name="Барсик", age=5, species="Кот")
    print(animal)  # Используется метод __str__
    print(repr(animal))  # Используется метод __repr__
    print(animal.make_sound())  # Неизвестный звук

    # Создаем объект дочернего класса
    dog = Dog(name="Шарик", age=3, breed="Лабрадор")
    print(dog)  # Используется метод __str__
    print(repr(dog))  # Используется метод __repr__
    print(dog.make_sound())  # Гав-гав!
    print(dog.fetch("мяч"))  # Шарик принес(ла) мяч!
    pass
