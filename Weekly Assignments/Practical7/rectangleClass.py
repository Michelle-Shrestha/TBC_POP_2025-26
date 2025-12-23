class Rectangle:

    def __init__(self,width=1.0, height=1.0):
        self.width = width
        self.height = height

    def getArea(self):
        area = self.width * self.height
        return area
    
    def getPerimeter(self):
        perimeter = 2*(self.width+self.height)
        return perimeter
    

obj1= Rectangle(width=4,height=40)
obj2= Rectangle(3.5,35.9)
area2 = obj2.getArea()
perimeter2 = obj2.getPerimeter()
print("Object 1: ")
print(f"Width of obj1:{obj1.width}\nHeight of obj1: {obj1.height}")
print(f"Area of Obj1: {obj1.getArea():.2f}")
print(f"Perimeter of Obj1: {obj1.getPerimeter():.2f}\n")

print("Object 2: ")
print(f"Width of obj1:{obj2.width}\nHeight of obj2: {obj2.height}")
print(f"Area of Obj2: {area2:.2f}")
print(f"Perimeter of Obj2: {perimeter2:.2f}\n")