# Write a program to sum a list with 4 numbers

n= int(input("How many number you want to sum :\t"))
numbers = []
for i in range(n):
    num = int(input("Enter number {}: ".format(i + 1)))
    numbers.append(num)
sum_of_numbers = sum(numbers)
print("The sum of the numbers is:", sum_of_numbers)
# This code takes 'n' numbers as input from the user, stores them in a list, and then calculates and prints the sum of those numbers.