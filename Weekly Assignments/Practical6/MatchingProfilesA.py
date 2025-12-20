sus_Dna = [2.3, 3.3, 4.5, 6.7, 7.8, 2.1, 3.2, 4.3, 5.2, 6.5]
cri_Dna = [2.3, 3.3, 4.5, 6.7, 7.8, 2.1, 3.2, 4.3, 5.2, 6.5]

match = True
for i in range (10):
    #checks if each dna is same or not
    if sus_Dna[i]!=cri_Dna[i]:
         match=False
         #breaks if any one chromosome doesnot match
         break

if match == True:
    print("Repeated offender: Two profile matches")

else:
    print("Profile doesnot match")
