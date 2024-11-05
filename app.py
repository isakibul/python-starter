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