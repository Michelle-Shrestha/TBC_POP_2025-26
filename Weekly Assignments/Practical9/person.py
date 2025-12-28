#Task 2.1 Person.py
class Person:
    def __init__(self,firstName="Mr", lastName="X", address= "Brostol"):
        #Private variables
        self.__firstName= firstName 
        self.__lastName= lastName
        self.__address= address

    #Setters
    def setFirstName(self,firstName):
        self.__firstName = firstName

    def setLastName(self, lastName):
        self.__lastName = lastName

    def setAddress(self,address):
        self.__address = address

    #Getters
    def getFirstName(self):
        return self.__firstName
    
    def getLastName(self):
        return self.__lastName
    
    def getAddress(self):
        return self.__address
    #returing string to display output 
    def __str__(self):
        return "\n"+"Person's name is "+ self.getFirstName()+ " "+self.getLastName()+"\nAddress is "+self.getAddress()
    
# Creating a person object with default values
print("Creating a person object with default values")
p=Person()

#Prints the default given arguments.
print(p.__str__())

#setting name and address
print("\nNow setting the names and address\n")
p.setFirstName("Abdur")
p.setLastName("Rakib")
p.setAddress("UWE Frenchay Campus 4QXX")

#Printing the information using __str__ method
print("Printing the information using __str__ method")
print(p)

#Creating another object by passing the values explicitly
print("\nCreating another Person object by passing the values explicitly")
p1=Person("Jun","Hong","UWE Frenchay Campus 3QXX")

#Printing the information using __str__method
print("\nPrinting the information using __str__ method")
print(p1.__str__())
