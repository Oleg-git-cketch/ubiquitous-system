usernames = []

while True:
    new_name = input('Введите имя: ')
    if new_name in usernames:
        print('Такой user имеется попробуйте другой')
    else:
        usernames.append(new_name)
        print('Username успешно добавлен!')
        print(usernames)