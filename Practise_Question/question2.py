# Write a Python program to check whether a number is positive, negative, or zero.
num = int(input("Enter a number to check if it is positive, negative, or zero: "))
if num > 0:
    print(num, "is a positive number")
elif num < 0:
    print(num, "is a negative number")
else:
    print(num, "is zero")