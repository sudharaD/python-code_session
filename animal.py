class Animal:
    def __init__(self, breed="Unknown"):
        self.breed = breed
        print("Animal class initialized")

    def move(self):
        print("Moving")

    def talk(self):
        print("Talking")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self, name="Unknown"):
        print("Dog class initialized")
        self.name = name

    def bark(self, bark_style="Unknown"):
        print(f"{self.name} --> {bark_style}")


huski = Dog("Honey")

huski.move()
huski.bark("Slowly")
huski.eat()

rot_w = Dog("B_Daddy")

rot_w.move()
rot_w.bark()
