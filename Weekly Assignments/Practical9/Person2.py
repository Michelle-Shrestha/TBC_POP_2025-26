class Person: 
    def __init__(self,firstName="Mr/Ms", lastName="X", address= "Bristol"): 
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
     
class Lecturer(Person): 
 
    def __init__(self,lecID=None,lecFirstName="Mr/Ms",lecLastName="X",lecAddress="Bristol"): 
        super().__init__(lecFirstName,lecLastName,lecAddress) 
 
        self.__lecturerID=lecID 
 
    #Setters 
    def setLecturerID(self,lecID): 
        self.__lecturerID=lecID 
     
    #Getters 
    def getLecturerID(self): 
        return self.__lecturerID   
     
    #Base class already have name and address getter setter and Lecturer class has inherited it so no need to  of new getter setter that's already in there 
     
    #Overiding Base class method 
    def __str__(self): 
        #Using base method  
        return (f"\nLecturer Name is {self.getFirstName()} {self.getLastName()}\n" 
                f"Address is {self.getAddress()}\n" 
                #Sub class method 
                f"Lecturer ID: {self.getLecturerID()}") 
 
#Person parent class 
class Student(Person): 
 
    def __init__(self,studentFirstName="Mr/Ms",studentLastName="X",studentAddress="Bristol",studentID=None): 
        # Calling parent class constructor 
        super().__init__(studentFirstName,studentLastName,studentAddress) 
 
        self.__studentID=studentID 
 
    #Setters 
    def setStudentID(self,lecID): 
        self.__studentID=lecID 
     
    #Getters 
    def getStudentID(self): 
        return self.__studentID   
     
    #Base class already have name and address getter setter and student class has inherited it so no need to  of new getter setter that's already in there 
     
    #Overiding Base class method 
    def __str__(self): 
        #Using base method  
        return (f"\nStudent Name is {self.getFirstName()} {self.getLastName()}\n" 
                f"Address is {self.getAddress()}\n" 
                #Sub class method 
                f"Student ID: {self.getStudentID()}") 
 
#Using Student class as it's base 
class GraduateStudentClass(Student): 
    def __init__(self,studentFirstName="Mr/Ms",studentLastName="X",studentAddress="Bristol",studentID=None,sFirstName="Mr/Ms",sLastName="X"): 
        super().__init__(studentFirstName,studentLastName,studentAddress,studentID) 
 
        self.__SuperviorFirstName= sFirstName 
        self.__SuperviorLastName= sLastName 
 
    #Setter 
    def setSupervisorFirstName(self,sFirstName): 
        self.__SuperviorFirstName = sFirstName 
 
    def setSupervisorLastName(self, slastName): 
        self.__SuperviorLastName= slastName 
    #Getter 
    def getSupervisorFirstName(self): 
        return self.__SuperviorFirstName 
 
    def getSupervisorLastName(self): 
        return self.__SuperviorLastName 
     
    def __str__(self): 
        #Using base(grandparent) method  
        return (f"\nGraduated Student Name is {self.getFirstName()} {self.getLastName()}\n" 
                f"Address is {self.getAddress()}\n" 
                f"Student ID: {self.getStudentID()}\n" 
                #sub class method with current object 
                f"Supervisor's name: {self.getSupervisorFirstName()} {self.getSupervisorLastName()}") 
 
p = Person("Abdur","Rakib","UWE Frenchay Campus 4QXX") 
print(p.__str__()) 
#Default lecturer name, address with id: 1 
lec = Lecturer(1) 
print(lec.__str__()) 
#Argumented passed to the constructor 
lec2= Lecturer(2,"Chris","Simons","UWE Frenchay Campus 4QXX") 
print(lec2.__str__()) 
student= Student("Peter","Miller","UWE Frechay Campus",5678) 
print(student.__str__()) 
gradStudent= GraduateStudentClass("Dan","Fielding","UWE Frenchay Campus",6789,"Jim","Smith") 
print(gradStudent.__str__())