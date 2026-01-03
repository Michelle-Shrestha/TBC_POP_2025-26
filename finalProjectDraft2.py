# Car Accessories and Parts Shop

class StockItem:
    stockCategory= "Car Accessories"
    #Constructor with dynamic type
    def __init__(self,stockCode:str=None,itemQuantity:int = 0,itemPrice:float = 0):
        self.__stockCode = stockCode
        self.__itemQuantity= itemQuantity
        self.__itemPrice = itemPrice

        #If no stock code added
        if not stockCode:
            raise ValueError ("Please enter the stock code!!!")

        #Remainder for no quantity and invalid price
        if itemQuantity<0:
            print(f"Invalid Quantity: {self.__itemQuantity}")
            raise ValueError("Quantity must be greater than 0!!!")

        if itemQuantity>100:
            raise ValueError("Inalid Quantity!!!\nQuantity must be less than or equal to 100!!!")
        if itemPrice<=0:
            raise ValueError("Invalid Price!!! Price must be greater than 0")

    #Setters
    def setStockCode(self,stockCode):
        #if empty value passed while setting new stock code
        if not stockCode:
            raise ValueError ("Please enter a valid stock code")
        self.__stockCode=stockCode
        return "Successfully set new code"

    def setItemQuantity(self,itemQuantity):
        #Raise error if quanty is negative else set quantity 
        if itemQuantity<0:
            raise ValueError ("Inalid Quantity!!!\nQuantity must be more than or equal to 1!!!")
        if itemQuantity>100:
            raise ValueError ("Inalid Quantity!!!\nQuantity must be less than or equal to 100!!!")
        self.__itemQuantity=itemQuantity
        return "Successfully set new quantity"

    def setItemPrice(self,itemPrice):
        if itemPrice<=0:
            raise ValueError ("Invalid Price!!!\n Price must be greater than 0!!!")
        self.__itemPrice = itemPrice
        return "Successfully set new price"

    #Getters
    def getStockCode(self):
        return self.__stockCode
    
    def getItemQuantity(self):
        return self.__itemQuantity
    
    def getItemPrice(self):
        #using python build in function
        #rounding price to two decimal example: 20.0/20.12
        return round(self.__itemPrice,2)
    
    def getStockName(self):
        return "Unknown Stock Name"
    
    def getStockDescription(self):
        return "Unknown Stock Description"
    #Vat method
    def getVAT(self):
        return 17.5
      
    #Methods 
    #Calculating price with vat
    def calculate_VAT(self):
        new_price = self.__itemPrice * (1+ (self.getVAT())/100)
        return round(new_price,2)
    
    def increaseStock(self,qty):
        ItemCapacity= 100-self.__itemQuantity
        if qty<1:
            raise ValueError ("Increased item must be greater than or equal to one")
        if qty>ItemCapacity:
            raise ValueError(f"Quantity Exceeds maximum holding capacity !!! You can add additional {ItemCapacity} only.")
        #Checks whether the total Item quantity is valid or not (1-100)
        if qty>0 and qty<=ItemCapacity:
            self.__itemQuantity += qty
            return f"{qty} Quantity Successfully Added!!! \nCurrent Quantity: {self.__itemQuantity}."

    def sellStock(self,qty):
        if qty<1:
            raise ValueError ("Selling quantity must be greater than or equal to 1!!!")
        if qty>self.__itemQuantity:
            raise ValueError (f"Low Stock!!! Available Quantity: {self.__itemQuantity}")
        # If stock to be sell is valid more than 1 and less or equal to the available stock
        if qty>0 and qty<=self.__itemQuantity:
            self.__itemQuantity-=qty
            return(f"{qty} Quantity Successfully Sold!!!\nCurrent Quantity: {self.__itemQuantity}")
    
    #dunder method (displays the item information)
    def __str__(self):
        return (
            f"\n\nPrinting item stock information: \n"
            f"Stock Category: {self.stockCategory}\n"
            f"Stock type: {self.getStockName()}\n"
            f"Description: {self.getStockDescription()}\n"
            f"Stock Code: {self.getStockCode()}\n"
            f"Price Without VAT: {self.getItemPrice()}\n"
            f"Price With VAT: {self.calculate_VAT()}\n"
            f"Total unit in stock: {self.getItemQuantity()}\n"
        )
# ------------------------------------------------ StockItem Class END----------------------------------------------------------------------

# ------------------------------------------------ NavSys Class Start ----------------------------------------------------------------------

class NavSys(StockItem):
    def __init__(self,stockCode:str, brand:str,itemQuantity:int=0, itemPrice:float=0):
        super().__init__(stockCode,itemQuantity,itemPrice)
        self.__brand = brand.title()
        #If not brand argument passed
        if not brand:
            raise ValueError("No brand Added!!! Please enter a valid Brand")


    #setter
    def setBrand(self,brand):
        #if not brand name given (empty argument passed)
        if not brand:
            raise ValueError ("Please enter a brand name!!!")
        self.__brand = brand
        return "New Brand name set successfully"
    
    #getter
    def getBrand(self):
        return self.__brand.title()

    #Overriding base class getters
    def getStockName(self):
        return "Navigation System"
    
    def getStockDescription(self):
        return "GeoVision Sat Nav"
    
    #overriding Base class __str__() method
    def __str__(self):
        return super().__str__() + f"Brand: {self.getBrand()}\n"

# ------------------------------------------------ NavSys Class End ------------------------------------------------------------------------


# -------------------------------------------------- Displaying Menu --------------------------------------------------------

def displayMenu():
    print(" ----------------------------------------------")
    print("|   Welcome to Car Parts and Accessories Shop  |")
    print(" ----------------------------------------------")
    print("|             1. Adding New  Items             |")
    print("|             2. Modifying Items               |")
    print("|             3. Increase Stock                |")
    print("|             4. Sell Stock                    |")
    print("|             5. Stock Details                 |")# __str__
    print("|             6. Exit                          |")
    print(" ----------------------------------------------")

def DisplayModifyingItems():
    print(" -----------------------")
    print("|     Modifying Items   |")
    print(" -----------------------")
    print("|  1. Set Stock Code    |")
    print("|  2. Set Item Quanity  |")
    print("|  3. Set Item Price    |")
    print("|  4. Set Brand         |")
    print("|  5. Exit              |")
    print(" -----------------------")

# ------------------------ USER LOGIN -------------------------------------------------------------

def login():
    print("        Please Login      ")
    try: 
        with open("login.txt","r") as fp:
            #Using dictionary for username and password
            log={}
            for line in fp:
                #splits the line by | 
                userN,pw = line.strip().split("|")
                log[userN]= pw
            while True:
                userName = input("Enter your username: ")
                #checks whether user exist or not
                if userName in log:
                    password = input("Enter your password: ")
                    #if userName exist then checks if password matches or not
                    if log[userName]==password:
                        print("\n     Login Successfull       \n")
                        return True
                    else:
                        print("Incorrect Password!!!\n")
                else:
                    print("Username not found\n")
    except FileNotFoundError as fpe:
        print(f"The Error is: {fpe}")

# --------------------------------------- MAIN MENU ------------------------------------------------------

def menu():
    if not login():
        return
    #no object created
    obj=None # To keep track of the stock item
    while True:
        displayMenu()
        try:
            choice= int(input("Please Enter Your Choice: "))
            if choice ==1:
                code = input("Enter the stock code: ")
                qty= int(input("Enter the item quantity: "))
                price = float(input("Enter the item price: "))
                brand = input("Enter the brand name: ")
                #Creating class object
                obj = NavSys(code,brand,qty,price)
                print(f"\nCreating a stock with {obj.getItemQuantity()} units {obj.getStockName()},\
 price {obj.getItemPrice()} each, item code {obj.getStockCode()} and brand {obj.getBrand()}\n")
            
            #Sub choice for setting new info
            elif choice == 2:
                #If no obj created before modifying
                if obj is None: 
                    print("\nItem doesnot exist. Please add an item!!!\n")
                    #to go to the main display menu
                    continue
                DisplayModifyingItems()
                #Sub choice for choice modifying items
                subChoice = int(input("Enter your chocie: "))
                if subChoice ==1:
                    newStockCode = input("Enter the new code for the item: ")
                    print(f"\n{obj.setStockCode(newStockCode)}\n")
                elif subChoice ==2:
                    newQty = int(input("Enter the new quantity for the item: "))
                    print(f"\n{obj.setItemQuantity(newQty)}]n")
                elif subChoice ==3:
                    newPrice = float(input("Enter the new price for the item: "))
                    print(f"\n{obj.setItemPrice(newPrice)}\n")
                elif subChoice==4:
                    newBrandName= input("Enter the new brand name: ")
                    print(f"\n{obj.setBrand(newBrandName)}\n")
                elif subChoice ==5:
                    continue
                else:
                    print("\nPlease choose from the given option 1-4 only!!!\n")

            elif choice==3:
                if obj is None: 
                    print("\nItem doesnot exist. Please add an item!!!\n")
                    #to go to the main display menu
                    continue
                increaseStock= int(input("Enter how many quantity you want to increase: "))
                print(obj.increaseStock(increaseStock))
            
            elif choice==4:
                if obj is None: 
                    print("\nItem doesnot exist. Please add an item!!!\n")
                    #to go to the main display menu
                    continue
                sellStock= int(input("Enter how many quantity you want to sell: "))
                print(obj.sellStock(sellStock))
            
            elif choice==5:
                if obj is None: 
                    print("\nItem doesnot exist. Please add an item!!!\n")
                    #to go to the main display menu
                    continue
                print(obj.__str__())

            elif choice==6:
                print("Exiting the program.....\nThank You\n")
                break
            else:
                print("Please choose from the given option 1-6 only!!!")   
                continue
                    

        except ValueError as ve:
            print (f"The Error is: {ve}")
        except Exception as e:
            print(f"The Error is: {e}")
        except FileNotFoundError as fpe:
            print (f"The Error is: {fpe}")

menu()