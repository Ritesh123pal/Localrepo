# define a circle class to create a circle with radiusr using a constructor. define the area() method of the class which calculates the area of circle. define a perimeter() method of class which allows you to calculate the perimeter of circle.
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return (22/7) * self.radius**2
    def perimeter(self):
        return 2*(22/7) * self.radius
c1=circle(35)        
print(c1.area())
print(c1.perimeter())
