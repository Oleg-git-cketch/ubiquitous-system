clients = {}
opened_rooms = [f"{i}{chr(letter)}" for i in range(1, 12) for letter in range(ord('А'), ord('Я') + 1)]
closed_rooms = []


def add_client(name, room):
    clients[name] = room
    opened_rooms.remove(room)
    closed_rooms.append(room)

def del_client(name):
    closed_rooms.remove(clients[name])
    opened_rooms.insert(clients[name] - 1, clients[name])
    clients.pop(name)

def move_client(name, new_room):
    if name in clients:
        old_room = clients[name]
        if new_room in opened_rooms:
            # Удаляем старый класс и добавляем новый
            del_client(name)
            add_client(name, new_room)
            print(f"Клиент {name} переведен из {old_room} в {new_room}.")
        else:
            print(f"Комната {new_room} уже занята или не существует.")
    else:
        print(f"Клиент с именем {name} не найден.")

def close_rooms():
    return closed_rooms
def open_rooms():
    return  opened_rooms


while True:
    choice = input('Введите действие: ')

    if choice.lower() == 'добавить':
        cl_name = input('Имя ученика: ')
        cl_room = (input('Введите номер и букву класса. Например (1А; 5Г): '))
        add_client(cl_name, cl_room)
        print(clients)
        if cl_room in opened_rooms:
            add_client(cl_name, cl_room)
            print(clients)
        else:
            print("Error")
    elif choice.lower() == 'перевести':
        cl_name = input('Имя клиента: ')
        if cl_name in clients:
            print(opened_rooms)
            new_room = input('Выберите новый номер: ')
            move_client(cl_name, new_room)
            print(clients)
        else:
            print('Такого клиента нет!')

    elif choice.lower() == 'исключить':
        cl_name = input('Имя клиента: ')
        if cl_name in clients:
            del_client(cl_name)
            print(clients)
        else:
            print('Такого ученика нет!')
    elif choice.lower() == 'классы':
        print(close_rooms())
        print(open_rooms())
    elif choice.lower() == 'выход':
        break

    else:
        print('Error')