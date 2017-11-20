class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2*(self.length+self.width)

    def __str__(self):
        return "Rectangle has a length of %.2f, a width of %.2f, an area of %.2f, and a perimeter of %.2f" % (self.length, self.width, self.are(), self.perimeter())

rect1 = Rectangle(10,20)
