class StockItem:
    stockCategory=  "Car Accessories"
    def __init__(self,stockCode,itemQuantity,itemPrice):
        self.__stockCode = stockCode
        self.__itemQuantity= itemQuantity
        self.__itemPrice = itemPrice

        #Remainder for no quantity 
        if itemQuantity>1:
            print(f"No Quantity: {self.__itemQuantity}")
            raise ValueError("Item out of stock!!!")

    #Setters
    def setStockCode(self,stockCode):
        self.__stockCode==stockCode
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
    def calc_VAT(self,vat=17.5):
        new_price = self.__itemPrice * (1+ vat/100)
    def increaseStock(self):
        pass
    def sellStock(self):
        pass
    def getStockName(self):
        return "Unknown Stock Name"
    def stockDescription(self):
        return "Uknown Stock Description"
    def __str__(self):
        pass


