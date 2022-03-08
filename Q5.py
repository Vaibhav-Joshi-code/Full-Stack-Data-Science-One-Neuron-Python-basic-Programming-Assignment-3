#5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000
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
k = []
for i in range(2,10001):
    if prime(i) == True:
        k.append(i)
print("All prime numbers under in the interval 1-10000 are: ",k)
