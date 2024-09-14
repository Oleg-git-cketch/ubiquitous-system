class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

rectangle = Rectangle(4, 5)
print(rectangle.area)

rectangle.width = 6
print(rectangle.area)