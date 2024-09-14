class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

    def Start(self):
        print('Автомобиль заведен')

    def Stop(self):
        print('Автомобиль заглушен')

chevrolet = Car(model='Jentra', color='Black', year=2021)