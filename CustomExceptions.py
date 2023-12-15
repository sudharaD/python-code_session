class InvalidNameException(Exception):
    def __init__(self, error):
        super(InvalidNameException, self).__init__(error)
        self.error_code = 7


class InvalidAgeException(Exception):
    def __init__(self, error):
        super(InvalidAgeException, self).__init__(error)
        self.error_code = 5


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    @staticmethod
    def get_person(name, age):
        if not name:
            raise InvalidNameException("Invalid Name")
        if age < 0 or age >= 100:
            raise InvalidAgeException("Invalid Age")
        return Person(name, age)


try:
    person = Person.get_person("Sudhara", 28)
    print(person)
except (InvalidNameException, InvalidAgeException) as e:
    print(f"Error: {e.error_code}")

print("Hello World")
