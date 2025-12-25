# Task 1

class ComputerC:

    def __init__(self,name,price):
        #initialising instance/member variable
        #Private variable
        self.__name = name 
        self.__price = price 

    #Setters
    #def setName(self,name):#assigns values to the constructor after being called
    #    self.__name=name

    #def setPrice(self,price):
    #    self.__price=price

    #getters
    def getName(self):
        return self.__name
    
    def getPrice(self):
        return self.__price
    
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
comp =ComputerC(computerName,computerPrice)
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
comp.__name = "Dell"
comp.__price = 890.90
comp.display()

# TASK 1.4
#The private variable can only be acessed by the class (mathod in that class) 
#that's why we cant acess and change the variable value directly using object 
#Using public methods we can get the private names but if we try to print it directly it'll give us error.

#Task 1.5
#Public method to access private variables
#comp.setName("Dell")
#comp.setPrice("399.99")
#comp.display()

# TASK 1.6
""".
We cant change the values of those member variable because they are private variable.
It cannot be directly access nor can be directly changed by creating the object.
Private variables can be access only within the Class not beyond(outside) it's scope. 
The only way to access and change it is by using public methods. 
"""