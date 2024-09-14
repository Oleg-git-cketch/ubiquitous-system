class Student:
    def __init__(self, name='ivan', groupNumber='10A', age=18):
        self.name = name
        self.groupnumber = groupNumber
        self.age = age

    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getGroupNumber(self):
        return self.groupnumber
    def setNameAge(self, name, age):
        self.name = name
        self.age = age
    def setGroupNumber(self, groupNumber):
        self.groupnumber = groupNumber

student1 = Student(name="Alice", age=20, groupNumber="10B")
student2 = Student(name="Bob", age=22, groupNumber="11A")
student3 = Student(name="Charlie", age=19, groupNumber="12C")
student4 = Student(name="Diana", age=21, groupNumber="10D")
student5 = Student(name="Eve", age=23, groupNumber="11B")

student1.setNameAge('Alex', 18)
student1.setGroupNumber('8B')

print(f"Студент 1: Name = {student1.getName()}, Age = {student1.getAge()}, Group Number = {student1.getGroupNumber()}")
print(f"Студент 2: Name = {student2.getName()}, Age = {student2.getAge()}, Group Number = {student2.getGroupNumber()}")
print(f"Студент 3: Name = {student3.getName()}, Age = {student3.getAge()}, Group Number = {student3.getGroupNumber()}")
print(f"Студент 4: Name = {student4.getName()}, Age = {student4.getAge()}, Group Number = {student4.getGroupNumber()}")
print(f"Студент 5: Name = {student5.getName()}, Age = {student5.getAge()}, Group Number = {student5.getGroupNumber()}")
print(f"Измененная информация о студенте 1: Имя = {student1.getName()}, Возрост = {student1.getAge()}, Номер класса = {student1.getGroupNumber()}")