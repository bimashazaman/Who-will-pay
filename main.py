
# It imports the random module.
import random

# Asking the user to input a string of names seperated by a comma.
names_string = input(('Give me everybodys names, seperated by a comma: '))

# It splits the string into a list of names.
names = names_string.split(', ')

# Getting the length of the list of names.
length_of_the_name_list = len(names)

# Generating a random number between 0 and the length of the list of names.
random_choice = random.randint(0, length_of_the_name_list -1) 

# Assigning the value of the list of names at the index of the random number to the variable
# person_who_will_pay.
person_who_will_pay = names[random_choice]

# Printing the value of the variable person_who_will_pay and the string " is going to buy the meal today
print(person_who_will_pay + " is going to buy the meal today")












