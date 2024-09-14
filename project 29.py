class Animal:
    def makesund(self, s):
        print(s)


class Horse(Animal):
    pass

pony = Horse()
pony.makesund('Igogo')