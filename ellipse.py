import math


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

c = Ellipse()
x = c.calculate_area()
y = c.calculate_perimeter()
print("area of ellipse is = % f" % (x))
print("perimeter of ellipse is = %f" % (y))

