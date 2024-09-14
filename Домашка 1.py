def summa(a, b):
    return a + b

while True:
    numbers = int(input('Введите первое число для сложения: '))
    numbers2 = int(input('Введите второе число для сложения: '))
    result = summa(numbers, numbers2)
    print(f'Результат сложения: {result}')