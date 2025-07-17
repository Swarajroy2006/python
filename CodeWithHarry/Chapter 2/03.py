# Check the type of variable assigned using input () function.

a = input("Enter a number: ")
print("The type of variable is:", type(a)) 
# This program prompts the user to input a number and prints the type of the variable.
# The input function returns a string, so the type will be <class 'str'>.

b = int(input("Enter Something: "))
print("The type of variable is:", type(b)) 
# This program prompts the user to input something and converts it to an integer.
# The type will be <class 'int'>.