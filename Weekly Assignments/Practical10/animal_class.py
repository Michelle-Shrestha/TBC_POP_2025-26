from abc import * 

class Animal(ABC):
    def __init__(self,numberOfLegs):
        self.__numberOfLegs = numberOfLegs
    #setter
    def setNumLegs(self,numberOfLegs):
        self.__numberOfLegs = numberOfLegs
    #getter
    def getNumLegs(self):
        return self.__numberOfLegs
    
    #abstract methods
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def walk(self):
        pass

class Pet(ABC):
    def __init__(self, name):
        self.__name = name.capitalize()

    def setName(self,name):
        self.__name= name.capitalize()

    def getName(self):
        return self.__name
    
    @abstractmethod
    def play(self):
        pass

class Cat(Animal,Pet):
    def __init__(self, name, numberOfLegs):
        #To call both constructor we need to specify constructor to call.
        #otherwise it'll call the 1st paramterised constructor which is Animal class
        # When parent class is called directly, we must pass self to know the current object(instance)
        Animal.__init__(self,numberOfLegs)
        Pet.__init__(self,name)
    #Abstract method of base class 
    def eat(self):
        print(f"{self.getName()} eats mice")

    def walk(self):
        print(f"{self.getName()} walks with {self.getNumLegs()} legs")

    def play(self):
        print(f"{self.getName()} plays with tail")

#Multiple inheritance
class Fish(Animal,Pet):
    def __init__(self, name, numberOfLegs):
        Animal.__init__(self,numberOfLegs)
        Pet.__init__(self,name)

    #Abstract method of base class 
    def eat(self):
        print(f"{self.getName()} eats plants")

    def walk(self):
        print(f"{self.getName()} can't walk")

    def play(self):
        print(f"{self.getName()} plays pokemon")

class Spider(Animal):
    def __init__(self, name="Spider", numberOfLegs=8):
        #No need for self cause super funtion
        # automatically passes the current instance(object)
        super().__init__(numberOfLegs)
        self.name = name

    #Abstract method of base class 
    def eat(self):
        print(f"{self.name} eats fly")

    def walk(self):
        print(f"{self.name} walks with {self.getNumLegs()} legs")

    

s= Spider()
c= Cat("Max",4)
f= Fish("Nemo",0)
s.eat()
s.walk()

#Polymorphism
for x in (c,f):
    x.eat()
    x.walk()
    x.play()