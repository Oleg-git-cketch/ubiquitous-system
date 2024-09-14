students = {}
opened_clases = [f"{i}{chr(letter)}" for i in range(1, 12) for letter in range(ord('А'), ord('Я') + 1)]
closed_clases = []

def add_students(name, room):
    if room in opened_clases:
        students[name] = room
        opened_clases.remove(room)
        closed_clases.append(room)
    else:
        print(f"Класс {room} уже занят или не существует.")

def del_students(name):
    if name in students:
        room = students[name]
        closed_clases.remove(room)
        opened_clases.append(room)
        students.pop(name)
    else:
        print(f"Ученик с именем {name} не найден.")

def move_students(name, new_room):
    if name in students:
        if new_room in opened_clases:
            del_students(name)
            add_students(name, new_room)
            print(f"Учений {name} переведен в {new_room}.")
        else:
            print(f"Класс {new_room} уже занят или не существует.")
    else:
        print(f"Ученик с именем {name} не найден.")

def close_class():
    return closed_clases
def open_class():
    return opened_clases

while True:
    choice = input('Введите действие: ')

    if choice.lower() == 'добавить':
        cl_name = input('Имя ученика: ')
        print(opened_clases)
        cl_room = input('Выберите класс (например, 1А): ')
        if cl_room in opened_clases:
            add_students(cl_name, cl_room)
            print('Успешно!')
            print(students)
        else:
            print("Ошибка")

    elif choice.lower() == 'исключить':
        cl_name = input('Имя ученика: ')
        del_students(cl_name)
        print(students)

    elif choice.lower() == 'перевести':
        cl_name = input('Имя ученика: ')
        if cl_name in students:
            print(opened_clases)
            new_room = input('Выберите новый класс (например, 2Б): ')
            move_students(cl_name, new_room)
            print(students)
        else:
            print(f"Ученик с именем {cl_name} не найден.")

    elif choice.lower() == 'классы':
        print(close_class())
        print(open_class())

    elif choice.lower() == 'выход':
        break

    else:
        print('Ошибка')