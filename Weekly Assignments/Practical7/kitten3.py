class Kitten:
    breed = "Abyssinian"

    #parameterised constructor
    def __init__(self,value=None):
        #initialising instance/member variable age
        self.age = value

    #an instance/member method
    def set_age(self,value):
        self.age = value

    def display_age(self):
        print(self.age)

kitt = Kitten(3)
kitt2 = Kitten(4)

#kitt3 = Kitten() works if during init value = None

kitt.display_age()
kitt2.display_age()

kitt.set_age(5)
kitt.display_age()

print(kitt.breed)
print(kitt2.breed)
#Breed is accessed using the class (all over the class)
print(Kitten.breed)
#instance variavle cannot be accessed via class (as its local variable for that instance)
#print(Kitten.age)

#Chaning the breed value
Kitten.breed = "American Bobtail"
print(kitt.breed)
print(Kitten.breed)
