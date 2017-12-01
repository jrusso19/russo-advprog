class Circle():
    def __init__(self, r):
        self.x = r

    def area(self):
        return (self.x**2)*3.14

    def perimeter(self):
        return 2*self.x*3.14

    def __str__(self):
        return "Circle has a radius of %.2f, an area of %.2f, and a perimeter of %.2f" % (self.x, self.area(), self.perimeter())

class Rectangle():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x*self.y

    def perimeter(self):
        return (2* self.x) + (2 * self.y)

    def __str__(self):
        return "Rectangle has a dimensions of x = %.2f and y = %.2f, an area of %.2f, and a perimeter of %.2f" % (self.x, self.y, self.area(), self.perimeter())

class Square(Rectangle):
    def __init__(self, x):
        self.x = x
        self.y = x

    def __str__(self):
        return "Square has a sidelength of %.2f, an area of %.2f, and a perimeter of %.2f" % (self.x, self.area(), self.perimeter())

class Righttriangle():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x*self.y

    def hypotenuse(self):
        return (self.x**2 + self.y**2)**0.5

    def perimeter(self):
        return self.x + self.y + self.hypotenuse()

    def __str__(self):
        return "Rectangle has a dimensions of x = %.2f and y = %.2f, an area of %.2f, and a perimeter of %.2f" % (self.x, self.y, self.area(), self.perimeter())

class Equilateralrighttriangle(Righttriangle):
    def __init__(self, x):
        self.x = x
        self.y = x


rect1 = Righttriangle(3,4)
equi = Equilateralrighttriangle(12)
print equi
