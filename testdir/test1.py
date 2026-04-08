class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

    def __add__(self,other):
        return self.width + other.width

r1 = Rectangle(5,7)
r2 = Rectangle(3,10)

print(r1.area())
print(r2.area())

print(r1+r2)