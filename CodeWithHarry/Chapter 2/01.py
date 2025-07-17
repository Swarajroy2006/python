# Write a python program to add two numbers
# and print the result.

a=int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("The sum is:", a + b)


# This program prompts the user to input two numbers and prints their sum.
# The input function is used to take user input, and the int function converts it to an integer.

def add_numbers(num1, num2):
    """Function to add two numbers."""
    return num1 + num2
print("The Sum is (By funcation)",add_numbers(a, b))
# This program defines a function to add two numbers and prints the result.
# The function takes two arguments, adds them, and returns the sum.