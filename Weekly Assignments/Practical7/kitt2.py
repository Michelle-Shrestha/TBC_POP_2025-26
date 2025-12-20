class Kitten:
    #Constructor
    def __init__(self,value):
        #Self parameter is a regerence to the current instance/object
        # and used to access variables that belongs to the class
        #Inititalizing instance/member variable age
        #self.age =1

        self.age = value

    #instance/member method
    def set_age(self,value):
        self.age = value

    #an instance/member method
    def display_age(self):
        #print(self.age)
        #print("Age Unknown")
        print("Your age: ",self.age)

#This invokes parameterised constructor
kitt=Kitten(3)
kitt2 = Kitten(4)
#kitt3= Kitten()

#calling the instance/member method using the object kitt
kitt.display_age()
kitt2.display_age()
kitt.display_age()

#kitt3.display_age()
"""Task 1.8: 
    No, the program doesnot work. We have created a parameterised constructor
    which ask value(argument) while calling the class. So, if we call the instance/object without
    value the program doesnot work and throws error.
    Therefore, to prevent it everytime we call the Class's object we must pass needed values. 
"""

#Setting kitt 1 age 5
kitt.set_age(5)
kitt.display_age()

"""Task 1.9:
    While only initialising the member variables using a parameterised constructor,
    we should alwaus pass argument. but by calling set_age method, if we want to later change (modify)
    age of the kitten instead of going through the kitt class constructor we can change it with
    the method which is more dynamic and functional as we dont need to reconstruct the object to change age.
"""