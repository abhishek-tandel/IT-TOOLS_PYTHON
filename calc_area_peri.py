import math


class Circle:
    
    def calculate_area(self):
        print("enter the radius of circle: ")
        self.s = float(input())
        area = 3.14*self.s*self.s
        print("area of circle is = % f" % (area))
        
    def calculate_perimeter(self):
        perimeter = 2*3.14*self.s
        print("perimeter of circle is = % f" % (perimeter))


class Rectangle:
    
    def calculate_area(self):
        print("enter the length of rectangle: ")
        self.a = float(input())
        print("enter the breadth of rectangle: ")
        self.b = float(input())
        area = self.a*self.b
        return(area)
    
    def calculate_perimeter(self):
        perimeter = 2*(self.a+self.b)
        return(perimeter)


class Ellipse:
 
    def calculate_area(self):
        print("enter the semimajor axis of ellipse: ")
        self.a = float(input())
        print("enter the semiminor axis of ellipse: ")
        self.b = float(input())
        area = 3.14*self.a*self.b
        return(area)
    
    def calculate_perimeter(self):
        perimeter = 2 * 3.14 * math.sqrt((self.a * self.a + self.b * 
                                         self.b) / (2))
        return(perimeter)


class Square:
    
    def calculate_area(self):
        print("Enter side of square:")
        self.s = float(input())
        area = self.s*self.s
        print("Area of Square is = %f" % (area))
        
    def calculate_perimeter(self):
        perimeter = 4*self.s
        print("Perimeter of Square is = %f" % (perimeter))
        
c = Circle()
c.calculate_area()
c.calculate_perimeter()

c = Rectangle()
x = c.calculate_area()
y = c.calculate_perimeter()
print("area of rectangle is = % f" % (x))
print("perimeter of rectangle is = % f" % (y))

c = Ellipse()
x = c.calculate_area()
y = c.calculate_perimeter()
print("area of ellipse is = % f" % (x))
print("perimeter of ellipse is = %f" % (y))

c = Square()
c.calculate_area()
c.calculate_perimeter()
