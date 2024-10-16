#A recap of functions in python

###############
#Functions
"""
A function is a block of code that performs a specific task.
It is executed when it is called.
Functions can take arguments/parameters and return values.

Arguement vs parameter
An argument is the ACTUAL VALUE passed to the function when it is called.
A parameter is a VARIABLE used to define a particular value in a function.
"""

#Creating a function
"""
To create a function, use the 'def' keyword followed by the function name and parentheses.
The code block is indented and contains the code to be executed
"""

def firstFunction():
    print ("First function created")

#Calling a function
firstFunction()         #Output: First function created

#Arguments
def secondFunction(name):
    print("Hello " + name)

secondFunction("John")  #Output: Hello John
secondFunction("Jane")  #Output: Hello Jane

def thirdFunction(name, age):
    print("Hello " + name + ", you are " + str(age) + " years old")

thirdFunction("John", 25)   #Output: Hello John, you are 25 years old
thirdFunction("Jane", 30)   #Output: Hello Jane, you are 30 years old

#Arbitrary Arguments, *args
"""
If you do not know how many arguments that will be passed into your function,
add an asterik (*) before the parameter name in the function definition.
This way the function will receive a tuple of arguments,
and can access the items accordingly.
"""

def fourthFunction(*names):
    print("The youngest child is " + names[2])

fourthFunction("John", "Jane", "Doe")  #Output: The youngest child is Doe

#Keyword Arguments, **kwargs
"""
You can also send arguments with the key = value syntax.
This way the order of the arguments does not matter.
"""

def fifthFunction(child3, child2, child1):
    print("The youngest child is " + child3)

fifthFunction(child1 = "John", child2 = "Jane", child3 = "Doe")  #Output: The youngest child is Doe

#Default Parameter Value
"""
You can set a default value for a parameter.
If the function is called WITHOUT the argument, it uses the default value.
"""

def sixthFunction(name = "John Doe"):
    print("Hello " + name)

sixthFunction("Jane Doe")       #Output: Hello Jane Doe
sixthFunction()                 #Output: Hello John Doe
sixthFunction("Marc Doe")       #Output: Hello Marc Doe

#Return Values
"""
To let a function return a value, use the return statement.
"""

def seventhFunction(x):
    return 5 * x

print(seventhFunction(3))       #Output: 15

#Using iterables as arguments
"""
You can use an iterable as an argument in a function.
"""

def eighthFunction(cars):
    for x in cars:
        print(x)

cars = ["GMC, Tesla, Ford, Chevrolet, Lexus"]
eighthFunction(cars)            #Output: GMC, Tesla, Ford, Chevrolet, Lexus

#Positional-Only Arguments
"""
You can specify that the parameters should be positional-only.
This means that the parameters must be passed by position and not by keyword.
To do this, you can use the '/' character with a comma before it. (, /)
"""

def ninthFunction(x, y, /):
    return x + y

print(ninthFunction(3, 4))      #Output: 7

#Keyword-Only Arguments
"""
You can specify that the parameters should be keyword-only.
This means that the parameters must be passed by keyword and not by position.
To do this, you can use the '*' character with a comma before it. (, *)
"""

def tenthFunction(*, x, y):
    return x + y

print(tenthFunction(x = 3, y = 4))      #Output: 7

#Combined Positional-Only and Keyword-Only Arguments
"""
You can specify that the parameters should be positional-only or keyword-only.
To do this, you can use the '/' and '*' characters with a comma before them. (, /, *)
"""

def eleventhFunction(a, b, /, c, d, *, e, f):
    return a + b + c + d + e + f

print(eleventhFunction(1, 2, 3, 4, e = 5, f = 6))      #Output: 21

#Recursion
"""
Recursion is a common mathematical and programming concept.
It means that a function calls itself.
"""

def twelfthFunction(n):
    if n > 0:
        result = n + twelfthFunction(n - 1)
    else:
        result = 0
    return result

print(twelfthFunction(5))       #Output: 15

#Lambda Function
"""
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
"""

thirteenthFunction = lambda x: x + 10
print(thirteenthFunction(5))    #Output: 15

"""
Use lambda functions when an anonymous function is required for a short period of time.
"""



