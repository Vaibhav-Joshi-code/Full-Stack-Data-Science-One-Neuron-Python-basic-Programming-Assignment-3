#4. Write a Python Program to Check Prime Number
x = int(input("Enter any number: "))
p = True
def prime(n):
    for i in range(2,n):
        if n%i == 0:
            p = False
            break
    else:
        p = True
        return p
        print(f"{n} is prime")
if prime(x) == True:
    print(f"{x} is prime")
else:
    print(f"{x} is not prime")
