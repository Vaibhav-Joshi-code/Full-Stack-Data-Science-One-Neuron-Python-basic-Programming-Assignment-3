#3. Write a Python Program to Check Leap Year
year = int(input("Enter any year: "))
if year%4 == 0:
    if (year%100 == 0 and year%400 == 0):
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
