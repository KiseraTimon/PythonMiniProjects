#A recap of scope concepts in python

###############
#Scope
"""
A variable is only available from inside the region it is created.
This is called scope.
"""

#Local Scope
"""
A variable created inside a function belongs to the local scope of that function,
and can only be used inside that function.
"""

def firstfunc():
    x = 300
    print(x)

firstfunc()  #Output: 300

#Function Inside Function
"""
As explained in the previous example, the variable x is not available outside the function,
but it is available for any function inside the function.
"""

def secondfunc():
    x = 300
    def innerfunc():
        print(x)
    innerfunc()

secondfunc()  #Output: 300

#Global Scope
"""
A variable created in the main body of the python code is a global variable
and belongs to the global scope.
Global variables are available from within any scope, global and local.
"""

x = 300

def thirdfunc():
    print(x)

thirdfunc()  #Output: 300

#Naming Variables
"""
If you operate with the same variable name inside and outside of a function,
Python will treat them as two separate variables,
one available in the global scope (outside the function) and one available in the local scope (inside the function).
"""

x = 300

def fourthfunc():
    x = 200
    print(x)

fourthfunc()  #Output: 200
print(x)  #Output: 300

#Global Keyword
"""
If you need to create a global variable, but are stuck in the local scope,
you can use the 'global' keyword.
"""

def fifthfunc():
    global x
    x = 300

fifthfunc()
print(x)  #Output: 300

"""
Also, use the 'global' keyword if you want to make a change to a global variable inside a function.
"""

x = 300

def sixthfunc():
    global x
    x = 200

sixthfunc()
print(x)  #Output: 200

#Nonlocal Keyword
"""
If you want to change a variable that is outside the local scope,
use the 'nonlocal' keyword.
"""

def seventhfunc():
    x = 300
    def innerfunc():
        nonlocal x
        x = 200
    innerfunc()
    return x

print(seventhfunc())  #Output: 200

"""
The 'nonlocal' keyword is used to work with variables inside nested functions,
where the variable should not belong to the inner function.
"""