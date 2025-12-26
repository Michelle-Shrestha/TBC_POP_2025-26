def user_input():
    sus=[]
    cri=[]
    #Taking input from the user in string and spliting them by space
    sus=input("Enter the 10 DNA of the suspect: ").split(" ")
    cri=input("Enter the 10 DNA of the criminal: ").split(" ")
    return sus,cri

def matchingProfiles(cri,sus):
    match = True
    for i in range (10):
        #checks if each dna is same or not
        if sus[i]!=cri[i]:
            match=False
            #breaks if any one chromosome doesnot match
            break
    return match

def main():
    sus_Dna, cri_Dna = user_input()
    match= matchingProfiles(sus_Dna,cri_Dna)
    if match == True:
        print("Repeated offender: Two profile matches")
    else:
        print("Profile doesnot match")

main()