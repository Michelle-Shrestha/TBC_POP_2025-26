class StockItem:
    stockCategory=  "Car Accessories"
    def __init__(self,stockCode,itemQuantity=0,itemPrice=0):
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
        return self.__itemPrice
    
    #Methods 

    #Calculating price with vat
    def calculate_VAT(self,vat=17.5):
        new_price = self.__itemPrice * (1+ vat/100)
        return new_price
    
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
            raise ValueError ("Invalid Quantity!!!\nQuantity must be greater than 0!!!")
        if qty>self.__itemQuantity:
            raise ValueError (f"Low Stock!!!\nAvailable Stock: {self.__itemQuantity}")
        # If stock to be sell is valid more than 1 and less or equal to the available stock
        if qty>0 and qty<=self.__itemQuantity:
            self.__itemQuantity-=qty
            return(f"{qty} Quantity Successfully Sold!!!\nCurrent Quantity: {self.__itemQuantity}")

    def getStockName(self):
        return "Unknown Stock Name"
    def getstockDescription(self):
        return "Unknown Stock Description"
    def __str__(self):
        pass


def displayMenu():
    print("--- Car Parts and Accessories Shop---")
    print("1. Adding New  Items                 ")
    print("2. Modifying Items                   ")
    print("5. Increase Stock                    ")
    print("5. Sell Stock                        ")
    print("6. Stock Details                     ")# __str__

try:
    s1 = StockItem("W101",10,1000)
    print(s1.stockCategory)
    print(s1.getStockName())
    print(s1.getstockDescription())
    print(s1.sellStock(0))
    print(s1.increaseStock(0))
    print(s1.calculate_VAT())
    
except ValueError as e:
    print(e)