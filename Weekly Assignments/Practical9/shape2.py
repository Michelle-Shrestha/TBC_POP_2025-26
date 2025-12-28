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

#print(rect.colour)
print("Color:",rect.getRectangleColour())
rect.display() #Overrides the base class method by the sub class.
print("\n")
sqr = Square()
sqr.display()
#the Square class doesnot overides the method of base class which is why 
#while instantiating and creating object it display's base class method and constructor

sqr.getRectangleColour()
"""
sqr object is calling the Rectangle class method, but the Square class is the sub class of Shape but the Rectangle class.
Therefore, it throws error while calling Rectangle class method by Squre class object.
"""