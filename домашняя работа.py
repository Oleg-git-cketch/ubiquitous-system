class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

def main():
    dog = Dog()
    cat = Cat()
    cow = Cow()

    print("Dog says:", dog.make_sound())
    print("Cat says:", cat.make_sound())
    print("Cow says:", cow.make_sound())


main()