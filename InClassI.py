# Stephanie Cheng
# CIS 41B Spring 2019
# In-class assignment I


# Part 1 of 1 - Basic Inheritance - Circle & Cylinder
import math
class Circle():
    
    def __init__(self, radius):
        self.radius = radius
        
    def getArea(self):
        return math.pi * (self.radius ** 2)
        
class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height
    
    def getVolume(self):
        return self.getArea() * self.height
    
c1 = Circle(4)
print("Circle area is:", round(c1.getArea(), 2))

cy2 = Cylinder(2, 5)
print("Cylinder volume is:", round(cy2.getVolume(), 2))