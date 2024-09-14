all_products = {'Весь склад': {}}
basket = {}
while True:
    admin = input('Что вы хотите сделать?: ')
    if admin.upper() == 'ДОБАВИТЬ':
        product_name = input('Введите название продукта: ')
        product_count = input('Введите количество: ')
        all_products['Весь склад'][product_name] = product_count
        print(all_products)
    elif admin.upper() == 'ПРОДУКТЫ':
        print(all_products)
    elif admin.upper() == 'ДОБАВИТЬ В КОРЗИНУ':
        product_name = input('Введите название продукта для добавления в корзину: ')
        if product_name in all_products['Весь склад']:
            add_product_to_basket = int(input('Введите количество: '))
            if product_name in basket:
                basket[product_name] += add_product_to_basket
            else:
                basket[product_name] = add_product_to_basket
            print('Продукт добавлен в корзину.')
            print(basket)
        else:
            print('Продукт не найден на складе.')
    elif admin.upper() == 'КОРЗИНА':
        print('Содержимое корзины:')
        print(basket)
    elif admin.upper() == 'ИЗМЕНИТЬ КОРЗИНУ':
        product_name = input('Введите название продукта для изменения в корзине: ')
        if product_name in basket:
                new_count = int(input('Введите новое количество: '))
                if new_count <= 0:
                    basket.pop(product_name)
                    print('Продукт удален из корзины.')
                else:
                    basket[product_name] = new_count
                    print('Количество продукта в корзине изменено.')
                print(basket)
        else:
            print('Продукт не найден в корзине.')
    elif admin.upper() == 'УДАЛИТЬ ИЗ КОРЗИНЫ':
        product_name = input('Введите название продукта для удаления из корзины: ')
        if product_name in basket:
            basket.pop(product_name)
            print('Продукт удален из корзины.')
            print(basket)
        else:
            print('Продукт не найден в корзине.')