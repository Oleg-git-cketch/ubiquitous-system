class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        return f"Brand: {self.brand}, Year: {self.year}"

class Car(Vehicle):
    def __init__(self, brand, year, num_doors):
        super().__init__(brand, year)
        self.num_doors = num_doors

    def display_info(self):
        return f"Car brand: {self.brand}, Year: {self.year}, Doors: {self.num_doors}"

class Motorcycle(Vehicle):
    def __init__(self, brand, year, has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar = has_sidecar

    def display_info(self):
        return f"Motorcycle brand: {self.brand}, Year: {self.year}, {'with sidecar' if self.has_sidecar else 'without sidecar'}"

def main():
    car = Car("Toyota", 2020, 4)
    motorcycle = Motorcycle("Harley-Davidson", 2022, True)
    print(car.display_info())
    print(motorcycle.display_info())

main()