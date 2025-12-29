#File handling
f = open("Weekly Assignments/Practical10/myFile.txt","r")
print(f.read())
f.close()
print()
f= open("Weekly Assignments/Practical10/yourFile.txt","r")
print(f.readline())
print(f.readline())
f.close()

try:
    f=open("Weekly Assignments/Practical10/yourFile1.txt","r")
    print(f.readline())
    f.close()

except FileNotFoundError as e:
    print(e)
