class Shapes:

    def __init__(self, length_of_sides):

        self.length_of_sides = length_of_sides

    def area(self):
        print("The area is")
        return self.length_of_sides * self.length_of_sides

    def perimeter(self):
        print("The perimeter is")
        return 4*self.length_of_sides

    # def num_of_sides(self):
    #     return 4

class Square(Shapes):
    pass


class Rectangle(Shapes):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("The area is")
        return self.length * self.width

    def perimeter(self):
        print("The perimeter is")
        return 2*self.length + 2*self.width


class Diamond(Shapes):

    def __init__(self, length, altitude):
        self.length = length
        self.altitude = altitude

    def area(self):
        print("The area is")
        return self.length * self.altitude

    def perimeter(self):
        print("The perimeter is")
        return 4*self.length

class Triangle(Shapes):

    def __init__(self, height, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
#         where side_b is the base
        self.side_c = side_c
        self.height = height

    def area(self):
        print("The area is")
        return (self.side_b*self.height)/2

    def perimeter(self):
        print("The perimeter is")
        return self.side_a + self.side_b + self.side_c

import math

class Circle(Shapes):
    def __init__(self, pi, r):
        self.pi = pi
        self.r = r

    def area(self):
        print("The area is")
        return self.pi*(math.pow(self.r, 2))

    def perimeter(self):
        print("The circumference using pi = 3.14159 is")
        return 2*self.pi*self.r

x = Circle(3.1415, 5)



print(x.perimeter())