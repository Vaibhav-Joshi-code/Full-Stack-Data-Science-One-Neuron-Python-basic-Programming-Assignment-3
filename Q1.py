#1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
x = int(input("Enter any number: "))
if x>0:
    print(f"{x} is positive")
elif x<0:
    print(f"{x} is negative")
else:
    print(f"{x} = 0")
