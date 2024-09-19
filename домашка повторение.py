# переменные
a = [1]
if a == 1:
    print('Hello, world!')
if a == 1:
    a.append(5)
    print(a)

# списки и кортежи
List = ['это', 'список']
Tuples = ('это', 'кортеж')
Tuples2 = 1, 'это' 'тоже' 'кортеж'
# .append() добавляет значение в конец списка
# .insert() добавляет значение в определенное место списка
# .extend() добавляет несколько значений в список

# циклы
for i in range(1, 11):
    print(i)
stop = 0
while True:
    print('Hello, world!')
    stop += 1
    if stop == 10:
        break

# словари
Dict = {'a': 'Hello, World!'}
print(Dict)
# .values выводит значение ключей
# .keys выводит ключи словаря
# .items выводит и ключи и значения словаря

# функции
def a():
    print(1 + 2)
i = lambda x:1+1 # анонимная функция
print(i)

# классы
class Numbers:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def addition(self):
        a = self.number1 + self.number2
        return a

numbers = Numbers(1, 2)
print(numbers.addition())

# наследование
class Parent:
    def Eyes(self, s):
        print(s)

class Children(Parent):
    pass

# super() включает в себя все атребуты родительского класса
#

