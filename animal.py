class Animal:
    def __init__(self, breed="Unknown"):
        self.breed = breed
        print("Animal class initialized")

    def move(self):
        print(f"{self.breed} --> Moving")

    def talk(self):
        print("Talking")

    def eat(self):
        print("Eating")


class Mamal:
    def __init__(self) -> None:
        print("Mamal class initialized")

    def feed(self):
        print("Feeding from Mamal")


class Dog(Animal, Mamal):
    def __init__(self, name="Unknown"):
        super(Dog, self).__init__("Dog")
        super(Animal, self).__init__()
        print("Dog class initialized")
        self.name = name

    def bark(self, bark_style="Unknown"):
        print(f"{self.name} --> {bark_style}")

    # Overriding
    def move(self):
        super(Dog, self).move()
        print("Move from Dog Class")

    # Overriding
    def eat(self):
        print("Eat from dog class")
        super(Dog, self).eat()

    # Overriding
    def feed(self):
        print("Feeding from dog class")
        super(Dog, self).feed()


huski = Dog("Honey")

huski.move()
huski.bark("Slowly")
huski.eat()

rot_w = Dog("B_Daddy")

rot_w.move()
rot_w.bark()
rot_w.feed()
