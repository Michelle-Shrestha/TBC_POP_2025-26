
#Practical 6, Part 4
#Michelle

print("Printing months from a list using a for loop: ")
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
"Aug", "Sep", "Oct", "Nov", "Dec"]
for x in months:
    #Skips april
    if x=="Apr":
        continue
    print(x)