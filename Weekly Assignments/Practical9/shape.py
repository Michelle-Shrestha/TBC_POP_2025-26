# TASK 1 (Modifying Class)

class Shape:
    #Constructor for Shape class
    def __init__(self,colour="Black"):
        self.colour =colour
        print("Shape constructor is called")

    #Method of Shape class
    def display(self):
        print("Shape is displaying")

    def getColour(self):
        return self.colour

class Rectangle (Shape):
    #Constructor for Rectangle class
    #Sub class constructor is called using 'super'
    def __init__(self):
        super().__init__()
        print("Rectangle constructor is called")

    #Method of Rectangle class
    # Overriding method of the base class
    def display(self):
        print("Rectangle is displaying")

    def getRectangleColour(self):
        #returns the base class color 
        return self.colour

class Square(Shape):
    pass

#shape = Shape()
#shape.display()
rect=Rectangle()

#Super class method
#rect.displayShape()
#Sub class method
#rect.displayRectangle()
"""
Subclass does not inherit the private members of it's base class, but private membera can be accessed by base class public or protected methods.
Therefore, using getRectangleColour() (returning the base class method).
While the Protected members can be accessed by the sub class directly.
"""
#print(rect.colour)
print("Color:",rect.getRectangleColour())
rect.display() #Overrides the base class method by the sub class.
"""
Instead of displaying the shape class's method output, it is displaying the rectangle class method output
because the sub class is overriding the base class's method.
"""

