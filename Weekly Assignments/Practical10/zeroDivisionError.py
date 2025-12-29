
def input_numbers():
    
    a = float(input("Enter first number: "))
    b= float(input("Enter second number: "))

    try:
        print(f"{a}/{b} is {a/b}")

    except ZeroDivisionError as exp:
        print("\n")
        print(exp)
        print("Cannot Divide by zero\n")
        input_numbers()

input_numbers()