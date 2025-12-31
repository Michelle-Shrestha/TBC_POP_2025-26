class StockItem:
    stockCategory=  "Car Accessories"
    #Constructor with dynamic type
    def __init__(self,stockCode:str,itemQuantity:int = 0,itemPrice:float = 0):
        self.__stockCode = stockCode
        self.__itemQuantity= itemQuantity
        self.__itemPrice = itemPrice

        #Remainder for no quantity 
        if itemQuantity<0:
            print(f"No Quantity: {self.__itemQuantity}")
            raise ValueError("Item out of stock!!!")

    #Setters
    def setStockCode(self,stockCode):
        self.__stockCode=stockCode
    def setItemQuantity(self,itemQuantity):
        self.__itemQuantity=itemQuantity
    def setItemPrice(self,itemPrice):
        self.__itemPrice = itemPrice

    #Getters
    def getStockCode(self):
        return self.__stockCode
    def getItemQuantity(self):
        return self.__itemQuantity
    def getItemPrice(self):
        #using python build in function
        #rounding price to two decimal example: 20.0/20.12
        return round(self.__itemPrice,2)
    
    #Methods 

    #Calculating price with vat
    def calculate_VAT(self,vat=17.5):
        new_price = self.__itemPrice * (1+ vat/100)
        return round(new_price,2)
    
    def increaseStock(self,qty):
        ItemCapacity= 100-self.__itemQuantity
        if qty<=0:
            raise ValueError ("Cannot add quantity less than 1!!!")
        if qty>ItemCapacity:
            raise ValueError(f"Excess Quantity!!! You can add additional {ItemCapacity} only.")
        #Checks whether the total Item quantity is valid or not (1-100)
        if qty>0 and qty<=ItemCapacity:
            self.__itemQuantity += qty
            return f"{qty}Quantity Successfully Added!!! \nCurrent Quantity: {self.__itemQuantity}."

    def sellStock(self,qty):
        if qty<=0:
            raise ValueError ("Invalid Quantity!!! Quantity must be greater than 0!!!")
        if qty>self.__itemQuantity:
            raise ValueError (f"Low Stock!!! Available Quantity: {self.__itemQuantity}")
        # If stock to be sell is valid more than 1 and less or equal to the available stock
        if qty>0 and qty<=self.__itemQuantity:
            self.__itemQuantity-=qty
            return(f"{qty} Quantity Successfully Sold!!!\nCurrent Quantity: {self.__itemQuantity}")

    def getStockName(self):
        return "Unknown Stock Name"
    
    def getstockDescription(self):
        return "Unknown Stock Description"
    
    #dunder method (displays the item information)
    def __str__(self):
        return (
            f"\n\nPrinting item stock information: \n"
            f"Stock Category: {self.stockCategory}\n"
            f"Stock type: {self.getStockName()}\n"
            f"Description: {self.getstockDescription()}\n"
            f"Stock Code: {self.getStockCode()}\n"
            f"Price Without VAT: {self.getItemPrice()}\n"
            f"Price With VAT: {self.calculate_VAT()}\n"
            f"Total unit in stock: {self.getItemQuantity()}\n"
        )


def displayMenu():
    print("--- Car Parts and Accessories Shop---")
    print("1. Adding New  Items                 ")
    print("2. Modifying Items                   ")
    print("5. Increase Stock                    ")
    print("5. Sell Stock                        ")
    print("6. Stock Details                     ")# __str__

def login():
    try: 
        with open("login.txt","r") as fp:
            #Using dictionary for username and password
            log={}
            for line in fp:
                #splits the line by | 
                userN,pw = line.strip().split("|")
                log[userN]= pw
                
            profileMatch = False
            while True:
                userName = input("Enter your username: ").capitalize()
                password = input("Enter your password: ")
                #checks whether user exist or not
                if userName in log:
                    #if userName exist then checks if password matches or not
                    if log[userName]==password:
                        print("Login Successfull")
                        break
                    else:
                        print("Incorrect Password!!!")
                else:
                    print("Username not found")
    except FileExistsError as fpe:
        print(f"Error: {fpe}")

login()

try:
    s1 = StockItem("W101",10,99.99)
    print(s1.stockCategory)
    print(s1.getStockName())
    print(s1.getstockDescription())
    print(s1.sellStock(2))
    print(s1.increaseStock(10))
    print(s1.calculate_VAT())
    print(s1.__str__())
    
except ValueError as e:
    print(e)