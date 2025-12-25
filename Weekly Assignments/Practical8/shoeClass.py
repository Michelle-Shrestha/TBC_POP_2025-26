class Shoe:
    #constructor
    def __init__(self,brand,size=None,price=1599):
        self.__brand = brand
        self.__size = size
        self.__price = price

    #Setters
    def setBrand(self,brand):
        self.__brand = brand

    def setSize(self,size):
        self.__size = size

    def setPrice(self,price):
        self.__price = price

    #getter
    def getBrand(self):
        return self.__brand
    
    def getSize(self):
        if self.__size == None:
            print("Please enter size!!!")
        else:
            return self.__size
        
    def getPrice(self):
        return self.__price
    
    def display(self):
        print("\nBrand: "+str(self.getBrand()).capitalize())
        print(f"Size: {self.getSize():}")
        print(f"Price: {self.getPrice():.2f}")

#Checking whether is valid brand or not
isValidBrand = False
while not isValidBrand: #when true
    shoeBrand= str(input("Enter shoe's brand name: "))

    if 2<=len(shoeBrand)<=10:
        isValidBrand= True

    else:
        print("You must enter a valid name between 2 and 10 chars length")

#Checking whether is valid shoe's size or not
isValidSize = False
while not isValidSize: #Price=True
    shoeSize=int(input("\nEnter shoe's size: "))

    if 35<=shoeSize<=45:
        isValidSize=True
    else:
        print("You must enter a valid size between 35-45")


#Checking whether is valid price or not
isValidPrice = False
while not isValidPrice: #Price=True
    shoePrice=float(input("\nEnter shoe's price: "))

    if 99.99<=shoePrice<=9999.99:
        isValidPrice=True
    else:
        print("You must enter a valid price between 99.99 and 9999.99")

#Creating object
shoe1= Shoe(shoeBrand,shoeSize,shoePrice)
#Displaying brand,size and price
shoe1.display()

#Creating second object
shoe2 = Shoe(shoeBrand,shoeSize)
shoe2.setBrand("Puma")
shoe2.setSize(37)
shoe2.display()