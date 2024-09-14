import requests

url = 'https://httpbin.org/post'
data = {
    'custname': 'Elon Musk',
    'custtel': '+123123123',
    'custemail': 'realelon@gmail.com',
    'size': 'large',
    'topping': 'cheese',
    'delivery': '21:00',
    'comments': 'I love pizza'
}

responce = requests.post(url, data=data)
print(responce)
