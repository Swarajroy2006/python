# Use comparison operator to find out whether ‘a’ given variable a is greater than  ‘b’ or not.


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a>b)
# This program prompts the user to input two numbers and checks if the first number is greater than the second.
# It prints True if 'a' is greater than 'b', otherwise it prints False.

if a > b:
    print("a is greater than b")   
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")
# This program compares two numbers input by the user and prints whether the first number is greater than