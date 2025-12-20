"""months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
"Aug", "Sep", "Oct", "Nov", "Dec"]
for i in range (12):
    print(f"Month: {months[i]}")"""

months = []
index = 0

#While loop for taking input
while index<12:
    m = input("Enter a month: ").capitalize()
    months.append(m)
    index+=1

#For loop for printing 
print("\nNow printing the months you entered: \n")
for x in range(12):
    print(f"Month: {months[x]}")