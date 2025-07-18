#  Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []
for i in range(6):
    mark = int(input("Enter the marks of student {}: ".format(i + 1)))
    marks.append(mark)
    marks.sort()
print("The marks of the students are:", marks)
