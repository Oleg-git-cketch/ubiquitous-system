class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

    def stop(self):
        print('Машина остановилась')

chevrolet = Car(model='Jentra', color='Black', year=2021)
chevrolet.stop()
