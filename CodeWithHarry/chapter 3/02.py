#Write a program to fill in a letter template given below with name and date.
#   letter = ''' 
#   Dear <|Name|>,
#   You are selected!
#   <|Date|>

letter = ''' 
Dear <|Name|>,
You are selected!
<|Date|> '''

input_name = input("Enter your name\t")
input_date = input("Enter date\t")

letter = letter.replace("<|Name|>", input_name)
letter = letter.replace("<|Date|>", input_date)
print(letter)
# This program takes a user's name and date, then fills in a letter template with those details