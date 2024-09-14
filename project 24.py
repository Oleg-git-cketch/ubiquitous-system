students = {}
opened_class = [i for i in range(1, 6) for j in range(ord('А'), ord('Е') + 1)]
closed_class = []


def add_student(name, room):
    students[name] = room
    opened_class.remove(room)
    closed_class.append(room)

def del_student(name):
    closed_class.remove(students[name])
    opened_class.insert(students[name] - 1, students[name])
    students.pop(name)

def transfer_student(name, new_class_number):
    if name in students:
        if new_class_number in opened_class:
            old_class_number = students[name]
            opened_class.append(old_class_number)
            closed_class.remove(old_class_number)
            students[name] = new_class_number
            opened_class.remove(new_class_number)
            closed_class.append(new_class_number)
            print(f"Студент {name} переведен в класс {new_class_number}.")
        else:
            print(f"Класс {new_class_number} уже занят или не существует.")

def show_rooms():
    return closed_class


while True:
    choice = input('Введите действие: ')

    if choice.lower() == 'добавить':
        student_name = input('Имя клиента: ')
        print(opened_class)
        cl_room = int(input('Выберите номер: '))
        add_student(student_name, cl_room,)
        print(students)
    elif choice.lower() == 'исключить':
        cl_name = input('Имя ученика: ')
        if cl_name in students:
            del_student(student_name)
            print(students)
        else:
            print('Такого ученика нет!')
    elif choice.lower() == 'изменить':
        name = input('Имя ученика: ')
        new_class_number = int(input('Введите номер класса:'))
        transfer_student(name, new_class_number)
    elif choice.lower() == 'номера':
        print(show_rooms())
    elif choice.lower() == 'выход':
        break

    else:
        print('Error')