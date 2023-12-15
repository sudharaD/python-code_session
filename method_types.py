class Person:
    name_list = ["sd", "dhana"]  # class attributes

    def __init__(self, name="Unknown") -> None:
        print("Person is created")
        self.name = name

    def print_name(self):  # instance function(method)
        print(f"{self.name}, created instance function(method)")

    @classmethod  # python decorators
    def get_name_list(cls):
        return cls.name_list

    @staticmethod
    def get_person():
        return Person()


sudhara = Person("Sudhara")
sudhara.print_name()
print(Person.name_list)  # class attributes can access using class name
print(Person.get_name_list())
Person.print_name(sudhara)  # when calling from a clss object should manually pass
person1 = Person.get_person()
print(person1.name)
