class Car:
    #attribute of car
    brand = "ToyCar"
    color = "White"

    #Car's constructor
    def __init__(self,door=5,price=20000):
        self.door=door
        self.price=price


    #Car's instance/ member method
    def startCar(self):
        print("Car has stated")

    def stopCar(self):
        print("Car has stopped")

    def setNumberofDoors(self,door):
        self.door = door

    def getNumberOfDoors(self):
        print(f"Number of doors: {self.door}")
    
    def setPrice(self,price):
        self.price=price

    def getPrice(self):
        print(f"Car's Price: {self.price}")

car1 = Car()
print("Car 1:")
#printing car1 details
car1.getNumberOfDoors()
car1.getPrice()
print("Car Color:",car1.color)
print(f"Car Brand: {car1.brand}")

print("\nCar 2:")
car2= Car()
#Changing cars door num price,color,brand
car2.setNumberofDoors(10)
car2.setPrice(50000)
car2.brand = "CarToy"
car2.color = "Maroon"
#printing car details
car2.getNumberOfDoors()
car2.getPrice()
print("Car Color:",car2.color)
print(f"Car Brand: {car2.brand}")