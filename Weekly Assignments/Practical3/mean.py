#WAP to read 10 numbers from the user & calculate their Arithmetic mean

def user_input():
  total = 0
  for i in range(1,11):
    num = float(input(f"Enter the number {i}: "))
    total=total+num
  return total 

def average(total):
  avg=total/10
  return avg

def main():
  total = user_input()
  avg = average(total)
  print(f"Average: {avg}")

main()