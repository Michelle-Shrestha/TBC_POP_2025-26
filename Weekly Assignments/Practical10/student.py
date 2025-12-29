# Abstract class should be derived from ABC class present in the abc module
# "" "" contains both abstract and non abstract method

from abc import * 

class Person (ABC):
    #Constructor
    def __init__(self,name,address):
        self.__name= name
        self.__address= address
    #Setters
    def setName(self, name):
        self.__name=name

    def setAddress(self,address):
        self.__address=address
    #Getters
    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address
    #Display
    def __str__(self):
        return f"Person Name: {self.getName()} and Address is: {self.getAddress()}"

    #Abstract method
    @abstractmethod
    def studentship(self):
        pass


class Student(Person):
    #Constructor
    def __init__(self, name, address,studentID):
        #Super automatically passes the current instance
        super().__init__(name, address)
        self.__studentID= studentID
    #Checking if the person is student or not
    def studentship(self):
        if self.__studentID==0:
            print("This person is Not a Student")

        else:
            print("This person is a student")

    # method overriding
    def __str__(self):
        return super().__str__()
    
stud1= Student("Peter Miller", "Frenchay Campus",0)
stud2= Student("Max Miller", "Glenside Campus",1234)

stud1.studentship()
print(stud1)
stud2.studentship()
print(stud2)

p = Person("Abstract Person","Heaven")

"""
An abstract class Person can't be instantiated (object creation is not possible).
Must be subclass which inherit abstract class and implement the abstract method.
"""