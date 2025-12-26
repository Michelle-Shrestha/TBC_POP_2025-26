sus=[]
cri=[]
#Taking input from the user in string and spliting them by space
sus=input("Enter the 10 DNA of the suspect: ").split(" ")
cri=input("Enter the 10 DNA of the criminal: ").split(" ")

match = True
for i in range (10):
    #checks if each dna is same or not
    if sus[i]!=cri[i]:
         match=False
         #breaks if any one chromosome doesnot match
         break

if match == True:
    print("Repeated offender: Two profile matches")

else:
    print("Profile doesnot match")
