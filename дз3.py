class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        result = self.a + self.b
        print(f'результат: {result}')

    def multiplication(self):
        result = self.a * self.b
        print(f'результат: {result}')

    def division(self):
        result = self.a / self.b
        print(f'результат: {result}')

    def subtraction(self):
        result = self.a - self.b
        print(f'результат: {result}')

results = Math(a=20, b=10)

results.addition()
results.multiplication()
results.division()
results.subtraction()

