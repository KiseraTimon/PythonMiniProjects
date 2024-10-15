#A recap of variables, data types, booleans and identifiers in python

#Simple use of variables
x = 5
y = "John"
z = 5.0

#Assigning multiple values
x,y,z = "Orange", 3, 44.7

#Casting variables
x = str(20)         #interpreted as '3'
y = int(30)         #interpreted as 30
z= float (30)       #interpreted as 30.0

#Booleans
bool(5>7)

#Notes
"""
Use type() function to obtain the data type of the variable
Variable identifiers are case sensitive

Using booleans:
- Any string is true except empty strings
- Any number is true, except 0
- Any list/set/tuple/dictionary is true except empty ones
- The keywords 'True' and 'False' are used to assign boolean values
"""