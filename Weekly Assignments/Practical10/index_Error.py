#Index error: Error which occurs when we try to access non exist index in the list (index out of range of that list)

try:
    a=['a','b','c']
    i = int(input("Enter the index of the element you want to print: "))
    print(a[i])
except LookupError:
    print("Index Error Exception: List index out of range!!!")
else:
    print("No error!")
    

