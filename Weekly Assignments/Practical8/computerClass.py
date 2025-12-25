# Task 1

class ComputerA:

    def __init__(self,name,price):
        #initialising instance/member variable
        self.name = name 
        self.price = price

    #Setters
    def setName(self,name):#assigns values to the constructor after being called
        self.name=name

    def setPrice(self,price):
        self.price=price

    #getters
    def getName(self):
        return self.name
    
    def getPrice(self):
        return self.price
    
    #An instance/member method
    def display(self):
        print("\nComputer's name is: " +str(self.getName()).capitalize()+ " It's price is: "+ str(self.getPrice()))

#User provides a valid computer name
isValidName = False

while not isValidName: #when true
    computerName= str(input("Enter computer's name: "))

    if 2<=len(computerName)<=10:
        isValidName= True

    else:
        print("You must enter a valid name between 2 and 10 chars length")

#User provides a valid computer price
isValidPrice = False

while not isValidPrice: #Price=True
    computerPrice=float(input("\nEnter computer's price: "))

    if 99.99<=computerPrice<=999.99:
        isValidPrice=True
    else:
        print("You must enter a valid price between 99.99 and 999.99")

#Creating the comp object based on user's input
comp =ComputerA(computerName,computerPrice)
comp.display()

#Setting a different computer name using the setName method
#comp.setName("Dell")
#Setting a new price using the setPrice method
#comp.setPrice("890.90")
#comp.display()
#Setting a new name
#comp.setName("Lenovo")

#Setting a different computer name by accessing the name variable which is public
#Direct method
comp.name = "Dell"
comp.price = 890.90
comp.display()