# print("Hello World!")



# number1, number2, name = 24, 22, "Sakibul Islam"
# print(number1, number2, name)



# Literals
# Literal are used to input fixed value in program
# name = "Sakibul Islam"
# Here name is a variable and "Sakibul Islam" is a literal



# Type conversion

# There are two type of conversion:

# Implicit conversion - automatic type conversion:
# int_num = 24
# float_num = 10.50
# sum = int_num+float_num
# print(sum)
# print(type(sum))

# Explicit conversion(Type casting) - manual type conversion:
# num_str = "10"
# num_int = 24
# print(type(num_int))
# num_str = int(num_str) - we can also use float(), str()
# add = num_str+num_int
# print(add)



# Python print with end() parameter
# print('Good Morning!', end= ' ')

# Python print with sep() parameter
# print('New Year', 2024, 'See you soon!', sep= '. ')

# Print concatenate string
# print("Sakibul" + " " + "Islam")

# Output formatting
# x=10
# y=20
# print('The value of x is {} and y is {}'.format(x,y))

# Python input
# name = input("Enter your name: ")
# print(name)



# Python operators
# Floor division - // - 10//3=9
# Power - ** - 4**2=16
# Exponent Assignment - **= - x**=3 - Output: 8

# Identify operator
# x1=5
# y1=5
# print(x1 is not y1)

# Membership operator
# message="Hello World"
# print("Hello" in message)
# print("World" not in message)



# Python content flow

# If...else statement
# id = int(input("Enter a number: "))
# if id == 30:
#     print("Sakib")
# elif id == 22:
#     print("Apon")
# else:
#     print("Kaium")

# Loop
# students = ['Sakib', 'Apon', 'Kaium', 'Piyas']
# for student in students:
#     print(student)

# name = "Sakibul"
# for alphabet in name:
#     print(alphabet)

# for i in range(10):
#     print(i)

# number = 1
# while number <=10:
#     print(number)
#     number = number+1

# number = int(input("Enter a number: "))
# while number != 0:
#     print(f"You have entered: {number}")
#     number = int(input("Enter a number: "))
# print("End of the loop")

# infinite loop
# age = 32
# while age > 18:
#     print('You can vote')

# for i in range(10):
#     if i == 3:
#         break/continue
#     print(i)

# Pass statement
# In Python programming, the pass statement is a null statement which can be used as a placeholder for future code.Suppose we have a loop or a function that is not implemented yet, but we want to implement it in the future. In such cases, we can use the pass statement.
# number = 10
# if number<10:
#     pass
# print("Hello")



# Python numbers, Type conversion and mathematics
# Python supports integers, floating-point numbers and complex numbers. They are defined as int, float, and complex classes in Python.

# num1 = 5
# num2 = 2.5
# num3 = 8+2j

# Number systems
# Binary - Ob or 0B
# Octal - 0o or 0O
#Hexadecimal - 0x or 0X

# print(0b1101011)  # prints 107
# print(0xFB + 0b10)  # prints 253
# print(0o15)  # prints 13

# Explicit type conversion
# num2 = int(-2.8)
# print(num2)  # prints -2

# num3 = float(5)
# print(num3) # prints 5.0

# num4 = complex('3+5j')
# print(num4)  # prints (3 + 5j)

# Python random module
# import random
# print(random.randrange(10, 20))

# list1 = ['a', 'b', 'c', 'd', 'e']
# print(random.choice(list1))

# random.shuffle(list1)
# print(list1)

# print(random.random()*10)

# Python mathematics
# import math
# print(math.pi)
# print(math.cos(math.pi))
# print(math.exp(10))
# print(math.log10(1000))
# print(math.sinh(1))
# print(math.factorial(6))



# Python list

# add element to list
# fruits = ['apple', 'banana', 'mango']
# fruits.append('cheery')
# print(fruits)

# fruits.remove('banana')
# print(fruits)

# print(len(fruits))
# for fruit in fruits:
#     print(fruit)

# append() - Adds an item to the end of the list
# extend() - Adds items of lists and other iterables to the end of the list
# insert() - Inserts an item at the specified index
# remove() - Removes the specified value from the list
# pop() - Returns and removes item present at the given index
# clear() - Removes all items from the list
# index() - Returns the index of the first matched item
# count() - Returns the count of the specified item in the list
# sort() - Sorts the list in ascending/descending order
# reverse() - Reverses the item of the list
# copy() - Returns the shallow copy of the list



# Python tuple

# Similar to python list. But the major difference is we cannot modify a tuple once it is created.

# numbers = (1, 2, -5)
# print(len(numbers))
# for number in numbers:
#     print(number)



# Python sets

# Collection of unique data, meaning that elements within a set cannot be duplicated.

# A set can have any number of items and they may be of different types (integer, float, tuple, string, etc.). But a set cannot have mutable elements like lists, sets or dictionaries as its elements.

# mixed_set = {'Hello', 101, -2, 'Bye'}
# print(mixed_set)

# empty_set = set()
# print('Data type of empty_set:', type(empty_set))

# empty_dictionary = { }
# print('Data type of empty_dictionary:', type(empty_dictionary))

# Let's see what will happen if we try to include duplicate items in a set.
# numbers = {2, 4, 6, 6, 2, 8}
# print(numbers)   # {8, 2, 4, 6}

# Add set item in python
# numbers.add(32)
# numbers.add(35)
# print(numbers)

# Update python set
# companies = {'Lacoste', 'Ralph Lauren'}
# tech_companies = ['apple', 'google', 'apple']
# using update() method
# companies.update(tech_companies)
# print(companies)
# Output: {'google', 'apple', 'Lacoste', 'Ralph Lauren'}

# Remove an element from a set
# languages = {'Swift', 'Java', 'Python'}
# print('Initial Set:',languages)
# removedValue = languages.discard('Java')
# print('Set after remove():', languages)

# Built-in functions with set
# print(all(languages)) - all() - Returns True if all elements of the set are true (or if the set is empty).
# print(any(languages)) - any() - Returns True if any element of the set is true. If the set is empty, returns False.
# print(enumerate(languages)) - enumerate() - Returns an enumerate object. It contains the index and value for all the items of the set as a pair.
# print(len(languages)) - len() - Returns the length (the number of items) in the set.
# print(max(languages)) - max() - Returns the length (the number of items) in the set.
# print(min(languages)) - min() - Returns the smallest item in the set.
# print(sorted(languages)) - sorted() - Returns a new sorted list from elements in the set(does not sort the set itself).
# print(sum(languages)) - sum() - Returns the sum of all elements in the set.

# Python set operations

# Union of two sets
# first set
# A = {1, 3, 5}
# second set
# B = {0, 2, 4}
# perform union operation using |
# print('Union using |:', A | B)
# perform union operation using union()
# print('Union using union():', A.union(B))

# Set insertion
# first set
# A = {1, 3, 5}
# second set
# B = {1, 2, 3}
# perform intersection operation using &
# print('Intersection using &:', A & B)
# perform intersection operation using intersection()
# print('Intersection using intersection():', A.intersection(B))

# Difference between two sets
# first set
# A = {2, 3, 5}
# second set
# B = {1, 2, 6}
# perform difference operation using &
# print('Difference using &:', A - B)
# perform difference operation using difference()
# print('Difference using difference():', A.difference(B))

# Set symmetric difference
# first set
# A = {2, 3, 5}
# second set
# B = {1, 2, 6}
# perform difference operation using &
# print('using ^:', A ^ B)
# using symmetric_difference()
# print('using symmetric_difference():', A.symmetric_difference(B))

# Check if two sets are equal
# first set
# A = {1, 3, 5}
# second set
# B = {3, 5, 1}
# perform difference operation using &
# if A == B:
#     print('Set A and Set B are equal')
# else:
#     print('Set A and Set B are not equal')



# Python dictionary
# A Python dictionary is a collection of items, similar to lists and tuples. However, unlike lists and tuples, each item in a dictionary is a key-value pair (consisting of a key and a value).

# Creating a dictionary
# country_capitals = {
#   "Germany": "Berlin", 
#   "Canada": "Ottawa", 
#   "England": "London"
# }
# printing the dictionary
# print(country_capitals)

# Access dictionary item
# country_capitals = {
#   "Germany": "Berlin", 
#   "Canada": "Ottawa", 
#   "England": "London"
# }
# access the value of keys
# print(country_capitals["Germany"])    # Output: Berlin
# print(country_capitals["England"])    # Output: London

# Add item to the dictionary
# country_capitals = {
#   "Germany": "Berlin", 
#   "Canada": "Ottawa", 
# }
# add an item with "Italy" as key and "Rome" as its value
# country_capitals["Italy"] = "Rome"
# print(country_capitals)

# Remove dictionary item
# country_capitals = {
#   "Germany": "Berlin", 
#   "Canada": "Ottawa", 
# }
# delete item having "Germany" key
# del country_capitals["Germany"]
# print(country_capitals)

# country_capitals = {
#   "Germany": "Berlin", 
#   "Canada": "Ottawa", 
# }
# clear the dictionary
# country_capitals.clear()
# print(country_capitals)

# Change dictionary items
# country_capitals = {
#   "Germany": "Berlin", 
#   "Italy": "Naples", 
#   "England": "London"
# }
# change the value of "Italy" key to "Rome"
# country_capitals["Italy"] = "Rome"
# print(country_capitals)

# Iterate through a dictionary
# country_capitals = {
#   "United States": "Washington D.C.", 
#   "Italy": "Rome" 
# }
# print dictionary keys one by one
# for country in country_capitals:
#     print(country)
# print()
# print dictionary values one by one
# for country in country_capitals:
#     capital = country_capitals[country]
#     print(capital)

# Find dictionary length
# country_capitals = {"England": "London", "Italy": "Rome"}
# get dictionary's length
# print(len(country_capitals)) #Output: 2
# numbers = {10: "ten", 20: "twenty", 30: "thirty"}
# get dictionary's length
# print(len(numbers)) #Output: 3
# countries = {}
# get dictionary's length
# print(len(countries)) #Output: 0

# Python dictionary methods
# pop() - Removes the item with the specified key.
# update() - Adds or changes dictionary items.
# clear() - Remove all the items from the dictionary.
# keys() - Returns all the dictionary's keys.
# values() - Returns all the dictionary's values.
# get() - Returns the value of the specified key.
# popitems() - Returns the last inserted key and value as a tuple.
# copy() - Returns a copy of the dictionary.

# Dictionary membership test
# file_types = {
#     ".txt": "Text File",
#     ".pdf": "PDF Document",
#     ".jpg": "JPEG Image",
# }
# use of in and not in operators
# print(".pdf" in file_types) #Output: True
# print(".mp3" in file_types) #Output: False
# print(".mp3" not in file_types) #Output: True



# Python string
# message = "I love Python."
# print(message[4])
# print(message[-4])
# print(message[0:4])

# In Python, strings are immutable. That means the characters of a string cannot be changed. For example,
# message = 'Hola Amigos'
# message[0] = 'H'
# print(message)

# However, we can assign the variable name to a new string. For example,
# message = 'Hola Amigos'
# # assign new string to message variable
# message = 'Hello Friends'
# print(message); # prints "Hello Friends"

# Python multiline string
# multiline string 
# message = """
# Never gonna give you up
# Never gonna let you down
# """
# print(message)

# Compare two string
# str1 = "Hello, world!"
# str2 = "I love Swift."
# str3 = "Hello, world!"
# compare str1 and str2
# print(str1 == str2)
# compare str1 and str3
# print(str1 == str3)

# Join two or more string
# greet = "Hello, "
# name = "Jack"
# using + operator
# result = greet + name
# print(result)

# Iterate through python string
# greet = 'Hello'
# iterating through greet string
# for letter in greet:
# print(letter)

# Python string length
# greet = 'Hello'
# count length of greet string
# print(len(greet))

# String membership test
# print('a' in 'program')
# print('at' not in 'battle')

# Methods of python string
# upper() - Converts the string to uppercase
# lower() - Converts the string to lowercase

# partition() - Returns a tuple
# name = "Sakibul Islam"
# print(name.partition(' '))

# replace() - Replaces substring inside
# text = 'bat ball balling'
# replace 'ba' with 'ro'
# replaced_text = text.replace('ba', 'ro')
# print(replaced_text)

# find() - Returns the index of the first occurrence of substring
# message = 'Python is a fun programming language'
# check the index of 'fun'
# print(message.find('fun'))

# rstrip() - Removes trailing characters
# title = 'Python Programming   '
# remove trailing whitespace from title
# result = title.rstrip()
# print(result)

# split() - Splits string from left
# text = 'Python is fun'
# split the text from space
# print(text.split())

# startswith() - Checks if string starts with the specified string
# message = 'Python is fun'
# check if the message starts with Python
# print(message.startswith('Python'))

# isnumeric() - Checks numeric characters
# pin = "523"
# checks if every character of pin is numeric 
# print(pin.isnumeric())

# index() - Returns index of substring
# text = 'Python is fun'
# find the index of is
# result = text.index('is')
# print(result)

# Escape sequence in Python
# example = "He said, "What's there?""
# print(example) # throws error
# escape double quotes
# example = "He said, \"What's there?\""
# escape single quotes
# example = 'He said, "What\'s there?"'
# print(example)

# Python string formatting
# name = 'Cathy'
# country = 'UK'
# print(f'{name} is from {country}')