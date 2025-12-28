# TASK 1 (Modifying Class)

class Shape:
    #Constructor for Shape class
    def __init__(self,colour="Black"):
        self.colour =colour
        print("Shape constructor is called")

    #Method of Shape class
    def displayShape(self):
        print("Shape is displaying")

    def getColour(self):
        return self.colour

class Rectangle (Shape):
    #Constructor for Rectangle class
    #Base class constructor is called using 'super'
    def __init__(self):
        super().__init__()
        print("Rectangle constructor is called")

    #Method of Rectangle class
    def displayRectangle(self):
        print("Rectangle is displaying")

    def getRectangleColour(self):
        return self.colour

#shape = Shape()
#shape.displayShape()
rect=Rectangle()
#Super class method
#rect.displayShape()
#Base class method
#rect.displayRectangle()
"""
The base class (Rectangle class) is calling the super class(Shape Class) constructor and method.
Therefore, while instantiating and creating object it is printing the super class constructor and method along with it's own.
"""
print("Color:",rect.getRectangleColour())
