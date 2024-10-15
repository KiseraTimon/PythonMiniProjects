#A recap of operators in python

#Arithmetic operators
"""
Operators used to perform mathematical operations
"""

x=5                     #initializing x
y=3                     #initializing y

x+y                     #Addition
x-y                     #Subtraction
x*y                     #Multiplication
x/y                     #Division
x%y                     #Modulus
x**y                    #Exponentiation
x//y                    #Floor division

#Assignment operators
"""
Operators used to assign values to variables
"""

x=5             #Same as x=5            #Assigns 5 to x
x+=3            #Same as x=x+3          #Adds 3 to x
x-=3            #Same as x=x-3          #Subtracts 3 from x
x*=3            #Same as x=x*3          #Multiplies x by 3
x/=3            #Same as x=x/3          #Divides x by 3
x%=3            #Same as x=x%3          #Modulus of x by 3
x//=3           #Same as x=x//3         #Floor division of x by 3
x**=3           #Same as x=x**3         #Exponentiation of x by 3
x&=3            #Same as x=x&3          #Bitwise AND of x by 3
x|=3            #Same as x=x|3          #Bitwise OR of x by 3
x^=3            #Same as x=x^3          #Bitwise XOR of x by 3
x>>=3           #Same as x=x>>3         #Right shift x by 3
x<<=3           #Same as x=x<<3         #Left shift x by 3
(x:=3)          #Same as x=x:3        #Assigns 3 to x, introduced in python 3.8, called the walrus operator

#Comparison operators
"""
Operators used to compare values
"""

x=5             #initializing x
y=3             #initializing y

x==y            #Equal to
x!=y            #Not equal to
x>y             #Greater than
x<y             #Less than
x>=y            #Greater than or equal to
x<=y            #Less than or equal

#Logical operators
"""
Operators used to combine conditional statements
"""

x=5             #initializing x
y=3             #initializing y

x>3 and y>3     #Returns True if both conditions are true
x>3 or y>3      #Returns True if one of the conditions is true
not(x>3)        #Returns False because x>3 is true

#Identity operators
"""
Operators used to compare objects
"""

x=5             #initializing x
y=3             #initializing y

x is y          #Returns True if both variables are the same object
x is not y      #Returns True if both variables are not the same object

#Membership operators
"""
Operators used to test if a sequence is present in an object
"""

x=5             #initializing x
y=[1,2,3,4,5]  #initializing y

x in y          #Returns True if x is present in y
x not in y      #Returns True if x is not present in y

#Bitwise operators
"""
Operators used to compare binary numbers
"""

x=5             #initializing x
y=3             #initializing y

x&y             #Bitwise AND
x|y             #Bitwise OR
x^y             #Bitwise XOR
~x              #Bitwise NOT
x<<2            #Bitwise left shift
x>>2            #Bitwise right shift

#Notes
"""
- Arithmetic operators are used to perform mathematical operations
- Assignment operators are used to assign values to variables
- Comparison operators are used to compare values
- Logical operators are used to combine conditional statements
- Identity operators are used to compare objects
- Membership operators are used to test if a sequence is present in an object
- Bitwise operators are used to compare binary numbers
"""

#Further technical analysis
"""
1. How shift operators work

The shift operators are used to move the bits of a number left or right.
The left shift operator (<<) moves the bits to the left by a specified number of positions.
The right shift operator (>>) moves the bits to the right by a specified number of positions.
The bits that are shifted out of the number are discarded.
The bits that are shifted in are zeros.
The shift operators are used to multiply or divide a number by a power of 2.

Demonstration
x=5
x<<2

The binary representation of 5 is 101.
Shifting 101 to the left by 2 positions gives 10100.
The decimal representation of 10100 is 20.
Therefore, x<<2 returns 20.

2. How the walrus operator works

The walrus operator (:=) is used to assign values to variables as part of an expression.
It assigns the value of the expression to the variable on the left.
The walrus operator is useful when the expression is complex and you want to avoid repeating it.
The walrus operator was introduced in Python 3.8.

Demonstration
x=5
y=3
(x:=x+y)

The value of x is 5.
The value of y is 3.
Adding x and y gives 8.
The value of x is updated to 8.
Therefore, (x:=x+y) returns 8.
"""