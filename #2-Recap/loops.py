#A recap of loops in python

###############
#If...else statement
"""
If...else statement is used to execute a block of code if a condition is true.
If the condition is false, another block of code can be executed
"""

#Example
x = 5
y = 3

if (x>y):
    print("The value of x is greater than y")
else:
    print("The value of y is greater than x")

#Example using elif
if (x>y):
    print("The value of x is greater than y")
elif (x<y):
    print("The value of y is greater than x")
else:
    print("The values of x and y are equal")

#Short hand if (Conditional expression/ternary operators)
if x>y: print("The value of x is greater than y")

#Short hand if...else (Conditional expression/ternary operators)
print("The value of x is greater than y") if x>y else print ("The value of y is greater than the value of x")

#Conditional statements with 'and' logical operator
a = 2000
b = 333
c = 5000

if a>b and b>c:
    print ("The value of a is the largest, followed by b, then c")

#Conditional statements with 'or' logical operator
if a>b or c>a:
    print("Either value of a or c is the largest, and b is the smallest")

#Conditional statements with 'not' logical operator
if not a>b:
    print("The value of a is not greater than b")

#Nested if (if statement within an if statement)
x = 20
if x>10:
    print("x is more than 10")
    if (x>25):
        print("x is more than 25")
    else:
        print("x does not exceed 25")

#Conditional statements with pass keyword
"""
If..else statements cannot be empty.
The pass keyword bypasses the statement if there is nothing to write
It does not produce an error
"""

a = 100
b = 200

if b>a:
    pass

###############
#While Loops
"""
While loop is used to execute a block of code as long as a condition is true
It is a primitive loop that is used when the number of iterations is unknown
"""

#Example
i = 1
while i<6:
    print(i)
    i = i+1

#Break statement
"""
Break statement is used to terminate the loop when a condition is met
"""

i = 1
while i<6:
    print(i)
    if i==3:
        break
    i = i+1

#Continue statement
"""
Continue statement is used to skip the current iteration of the loop
It moves to the next iteration
"""

i = 0
while i<6:
    i = i+1
    if i==3:
        continue
    print(i)

#Else statement
"""
Else statement is used to execute a block of code after the loop has finished
"""

i = 1
while i<6:
    print(i)
    i = i+1
else:
    print("i is no longer less than 6")


###############
#For Loops
"""
For loop is used to iterate over a sequence (list, tuple, dictionary, set, string)
It is used when the number of iterations is known
"""

#Example
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#Looping through a string
for x in "banana":
    print(x)

"""
NOTE: The for loop does not require an indexing variable to set the number of iterations
It can also work with break, continue, pass and else statements
"""

#Range function
"""
Range function is used to generate a sequence of numbers
It is used in for loops
"""

for x in range(6):      #Generates numbers from 0 to 5
    print(x)

#Range function with start parameter
for x in range(2,6):    #Generates numbers from 2 to 5
    print(x)

#Range function with increment parameter
for x in range(2,30,3): #Generates numbers from 2 to 30, incrementing by 3
    print(x)

#Nested loops
colors = ["red", "blue", "green"]
weather = ["sunny", "rainy", "cloudy"]

for x in colors:
    for y in weather:
        print(x,y)


###############
#Additional notes
"""
- For loops are used to iterate over a sequence
- While loops are used to execute a block of code as long as a condition is true
- Break statement is used to terminate the loop when a condition is met
- Continue statement is used to skip the current iteration of the loop
- Else statement is used to execute a block of code after the loop has finished
- Pass keyword bypasses the statement if there is nothing to write
- Range function is used to generate a sequence of numbers
- Nested loops are used to iterate over multiple sequences
"""