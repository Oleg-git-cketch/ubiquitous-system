class Worker:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class Admin(Worker):
    def prosmotr(self):
        print(self.name)
        print(self.position)

text = Worker('Jordan', 'creater')

