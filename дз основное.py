class Dog:
    def __init__(self, name="Unknown", age=0, breed="Unknown"):
        self.name = name
        self.age = age
        self.breed = breed

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Breed: {self.breed}")



my_dog = Dog(name="Rex", age=5, breed='Husky')
my_dog.display_info()

another_dog = Dog(name="Bella", age=3, breed='German shepherd')
another_dog.display_info()
