def spam1(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

print(spam1(name= 'my1', age= 23))