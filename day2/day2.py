# Exercise 1
# Write a program that takes in a user input and prints out how many vowels are in the response

# "Example" -> 3
# "Hello World" -> 3
# "Brian" -> 2
# "This is a longer response" -> 8

import re

user_input = input('MAGIC TIME! Tell me a new word: ').lower()

print(user_input.replace(' ',''))

if user_input.replace(' ','').isalpha():
    print(len(re.findall(r'[a,e,i,o,u]', user_input)))
else:
    user_input = input('Enter a word so I can do my magic!: ').lower()
    print(len(re.findall(r'[a,e,i,o,u]', user_input)))
    
# It breaks if the input has a number though, for example 'this has 4 vowels'

# Exercise 2

# Using list comprehension, create a list of names of 4 letters or more and capitalize each name

names1 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 'bob', 'kevin']

names2 = [x.capitalize() for x in names1 if len(x) >= 4]
print(names2)

# Bonus Challenge
names3 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']

# # use the isdigit to filter the numbers
names4 = [x.capitalize() for x in names3 if not str(x).isdigit() and len(x) >=4]

print(names4)