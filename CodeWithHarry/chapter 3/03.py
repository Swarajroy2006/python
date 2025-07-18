# Write a program to detect double space in a string.

string = input("Enter a string: ")

print(string.find("  "))  # This will return the index of the first occurrence of double space or -1 if not found
if "  " in string:
    print("Double space detected")
else:
    print("No double space detected")
# This program checks if a user-inputted string contains double spaces and prints a message accordingly