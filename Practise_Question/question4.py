# Write a Python program to find the sum of digits of a 3-digit number.

num = int(input("Enter a 3-digit number: "))

hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10

sum = hundreds + tens + ones

print("Sum of digits:", sum)