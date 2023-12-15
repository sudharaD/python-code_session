class Person:
    def __init__(self, name) -> None:
        self.name = name
        self.__age = 25  # Privete
        self._city = "Colombo"  # Protected

    def _student_age(self) -> int:
        return 25

    def sleep(self):
        print(f"{self.name} --> sleeping")

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age


class Student(Person):
    def __init__(self, name):
        super(Student, self).__init__(name)

    def print_city(self):
        print(self._city)

    def _student_age(self) -> int:
        age = super(Student, self)._student_age()
        return age - 5


sudhara = Person("Sudhara")
sudhara.sleep()
print(sudhara.get_age())
sudhara.set_age(30)
print(sudhara.get_age())

student1 = Student("Dhananjaya")
student1.print_city()
print(student1._student_age())
