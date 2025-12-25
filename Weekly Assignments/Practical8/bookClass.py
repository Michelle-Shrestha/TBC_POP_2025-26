class Book:
    #constructor
    def __init__(self,isbn,title,author=None,year=None):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__year = year

    #Setters
    def setISBN(self,isbn):
        self.__isbn = isbn

    def setTitle(self,title):
        self.__title = title

    def setAuthor(self,author):
        self.__author = author

    def setYear(self,year):
        self.__year = year

    #Getters
    def getISBN(self):
        return self.__isbn
    
    def getTitle(self):
        return self.__title
    
    def getAuthor(self):
        if self.__author == None:
            return ("Author name not provided!!!")
        else:
            return self.__author
        
    def getYear(self):
        if self.__year == None:
            return ("Published Year not provided!!!")
        else:
            return self.__year
    # Book class instance/member method which displays the info    
    def display(self):
        print("\nTitle: "+str(self.getTitle()).capitalize())
        print(f"ISBN Number: {self.getISBN()}")
        print(f"Author: {self.getAuthor().capitalize()}")
        print(f"Published Year: {self.getYear()}")


#Checking whether the inputs are valid or not
isValidTitle = False
while not isValidTitle: #when true
    title= str(input("Enter book's title: "))

    if 3<=len(title)<=20:
        isValidTitle= True

    else:
        print("You must enter a valid title between 3 and 20 chars length")

isValidISBN = False
while not isValidISBN: #when true
    isbn_no= input("Enter book's ISBN number: ")

    #checking it's length and and whether the given input is numeric or not
    if len(isbn_no)==13 or len(isbn_no)==10 and isbn_no.isdigit():
        #changing string into integer
        isbn_no=int(isbn_no)
        isValidISBN= True

    else:
        print("You must enter a valid ISBN number of 10 or 13 chars length")

isValidAuthor = False
while not isValidAuthor: #when true
    author= str(input("Enter book's author name: "))

    if 5<=len(author)<=35:
        isValidAuthor= True

    else:
        print("You must enter the valid Author name between 5 and 35 chars length")

isValidYear = False
while not isValidYear:
    year= input("Enter the published year: ")
    #checking it's length and and whether the given input is numeric or not
    if 3<=len(year)<=4 and year.isdigit():
        #converting string into int
        year = int(year)
        #checking of year
        if 600<=year<=2025:
            isValidYear = True
    else:
        print("You must enter valid year between 600 to 2025")

#Creating objects
book1=Book(isbn_no,title,author,year)
book1.display()

book2=Book(isbn_no,title)
#using class method to access private variable
book2.setISBN(9781784752637)
book2.setTitle("To Kill a Mocking Bird")
book2.setAuthor("Harper Lee")
book2.display()

print(book1.__author())