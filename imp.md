### Assigning multiple values to multiple variables
a, b, c = 5, 3.2, 'Hello'
print(a)
print(b)
print(c)

site1 = site2  = 'python.com'
print(site1)
print(site2)




### Python constants
Create a constant.py:
# declare constants 
PI = 3.14
GRAVITY = 9.8
Create a main.py:

# import constant file we created above
import constant
print(constant.PI) # prints 3.14
print(constant.GRAVITY) # prints 9.8




### Literal Collections
# list literal
fruits = ["apple", "mango", "orange"] 
print(fruits)

# tuple literal
numbers = (1, 2, 3) 
print(numbers)

# dictionary literal
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} 
print(alphabets)

# set literal
vowels = {'a', 'e', 'i' , 'o', 'u'} 
print(vowels)




### Data Type
# List
It's basically array.

# Tuple
Tuple is an ordered sequence of items same as a list. The only difference is that tuples are immutable. Tuples once created cannot be modified.

In Python, we use the parentheses () to store items of a tuple. For example,
product = ('Xbox', 499.99)
print(product[0])

# Set
student_id = {112, 114, 116, 118, 115}
print(student_id)

# Dictionary
Same as object.




### Type Conversion
-Implicit Conversion - automatic type conversion
-Explicit Conversion - manual type conversion




### Arithmetic Operators
// - floor division - 10 // 3 = 3
** - power - 4 ** 2 = 16

# identity operators
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is not y1)  # prints False
print(x2 is y2)  # prints True
print(x3 is y3)  # prints False

# membership operators
message = 'Hello world'
dict1 = {1:'a', 2:'b'}

print('H' in message)  # prints True
print('hello' not in message)  # prints True
print(1 in dict1)  # prints True
print('a' in dict1)  # prints False




### Scope and Namespace
# global_var is in the global namespace
global_var = 10

def outer_function():
    #  outer_var is in the local namespace 
    outer_var = 20

    def inner_function():
        #  inner_var is in the nested local namespace 
        inner_var = 30

        print(inner_var)

    print(outer_var)

    inner_function()

print(global_var)

outer_function()

Output:
10
20
30

In the above example, there are three separate namespaces: the global namespace, the local namespace within the outer function, and the local namespace within the inner function.

Here,

global_var - is in the global namespace with value 10
outer_val - is in the local namespace of outer_function() with value 20
inner_val - is in the nested local namespace of inner_function() with value 30
When the code is executed, the global_var global variable is printed first, followed by the local variable: outer_var and inner_var when the outer and inner functions are called.

# use of global keyword
global_var = 10

def my_function():
    # define local variable
    local_var = 20

    # modify global variable value 
    global global_var
    global_var = 30

print(global_var)

my_function()

print(global_var)

Output:
10
30

Here, when the function is called, the global keyword is used to indicate that global_var is a global variable, and its value is modified to 30.

So, when the code is executed, global_var is printed first with a value of 10, then the function is called and the global variable is modified to 30 from the inside of the function.

And finally the modified value of global_var is printed again.
