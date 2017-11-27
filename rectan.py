class Rectangle():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x*self.y

    def perimeter(self):
        return 2*(self.x+self.y)

    def __str__(self):
        return "Rectangle has a length of %.2f, a width of %.2f, an area of %.2f, and a perimeter of %.2f" % (self.x, self.y, self.area(), self.perimeter())
class Square(Rectangle):
    def __init__(self, x):
        self.x = x
        self.y = x



rect1 = Rectangle(100,20)
print rect1
