previousMR = int(input("Enter the previous meter reading: "))
currentMR = int(input("Enter the current meter reading: "))
day = int(input("Enter the day of the meter reading: "))
month = int(input("Enter the month of the meter reading: "))

if(previousMR<0 or previousMR>9999):
    print("\nError: Previous meter reading out of range!!!\n")

if(currentMR<0 or currentMR>9999):
    print("\nError: Curremt meter reading out of range!!!\n")

if(previousMR>currentMR):
    print("\nError: Previous reading greater than current reading.\n")
else:
    electricity_used = currentMR-previousMR
    if (electricity_used>1000):
        print("\nError: Electricity used is more than 1000\n")
    
if month<1 or month >12:
    print("Error: Month should be 1-12!!")
else:
    #Months which have 31 days
    if month in [1,3,5,6,8,10,12]: 
        #if days is not 31
        if day!=31:
            print(f"\nError: Month {month} have 31 days!!!")
    #Months which have 30 days
    if month in [4,6,9,11]: 
        #if days is not 30
        if day!=30:
            print(f"\nError: Month {month} have 30 days!!!")
    #Months which have 29 days
    if month ==2: 
        #if days is not 29
        if day!=29:
            print(f"\nError: Month {month} have 29 days!!!")
