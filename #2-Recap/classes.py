#A recap of classes, objects and basic OOP principles in python

###############
#Classes
"""
A class is a blueprint for creating objects (a particular data structure),
providing initial values for state (member variables or attributes),
and implementations of behavior (member functions or methods).
"""

#Creating a class
"""
To create a class, use the 'class' keyword followed by the class name.
The code block is indented and contains the class variables and methods.
"""

class Person:
    name = "John"

#Creating an object
"""
An object is an instance of a class.
To create an object, use the class name followed by parentheses.
"""

p1 = Person()
print(p1.name)  #Output: John

#The __init__() function
"""
The __init__() function is a built-in function in python.
It is called when the class is being initiated.
It is used to assign values to object properties.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def namefunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)

print(p1.name)  #Output: John
print(p1.age)   #Output: 36
p1.namefunc()     #Output: Hello my name is John

#Object Methods
"""
Objects can also contain methods.
Methods in objects are functions that belong to the object.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def namefunc(self):
        print("Hello my name is " + self.name)
    
    def agefunc(self):
        print("I am " + str(self.age) + " years old")

p1 = Person("John", 36)

p1.namefunc()     #Output: Hello my name is John
p1.agefunc()      #Output: I am 36 years old

#The self parameter
"""
The self parameter is a reference to the current instance of the class,
and is used to access variables that belong to the class.
It does not have to be named 'self', you can call it whatever you like,
but it has to be the first parameter of any function in the class.
"""

#Modify object properties
"""
You can modify object properties by reassigning new values to the object property.
"""

p1.age = 40
p1.agefunc()      #Output: I am 40 years old

#Delete object properties
"""
You can delete object properties using the 'del' keyword.
"""

del p1.age
#p1.agefunc()      #This will raise an error

#Delete objects
"""
You can delete objects using the 'del' keyword.
"""

del p1

#The pass statement
"""
The pass statement is used as a placeholder for future code.
When the pass statement is executed, nothing happens.
"""

class Person:
    pass

#Inheritance
"""
Inheritance is a way to form new classes using classes that have already been defined.
The newly formed classes are called derived classes, the classes that we derive from are called base classes.
"""

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

x.printname()  #Output: Mike Olsen

#Add properties
"""
You can add properties to a class or object using the 'setattr()' method.
"""

setattr(x, "age", 36)
print(x.age)  #Output: 36

#Delete properties
"""
You can delete properties of a class or object using the 'delattr()' method.
"""

delattr(x, "age")
print(x.age)  #This will raise an error

#The super() function
"""
The super() function is used to give access to methods and properties of a parent or sibling class.
"""

#Multiple Inheritance
"""
Multiple inheritance is a feature in which a class can inherit
attributes and methods from more than one parent class.
"""

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

class Teacher(Person):
    def __init__(self, fname, lname, subject):
        super().__init__(fname, lname)
        self.subject = subject

class TeachingAssistant(Student, Teacher):
    def __init__(self, fname, lname, year, subject):
        Student.__init__(self, fname, lname, year)
        Teacher.__init__(self, fname, lname, subject)

y = TeachingAssistant("Mike", "Olsen", 2019, "Maths")

y.printname()  #Output: Mike Olsen

#Method Overriding
"""
Method overriding is a feature that allows a subclass to provide a specific implementation of a method
that is already provided by one of its parent classes.
"""

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    
    def printname(self):
        print(self.firstname, self.lastname, self.graduationyear)

z = Student("Mike", "Olsen", 2019)

z.printname()  #Output: Mike Olsen 2019

#Encapsulation
"""
Encapsulation is an object-oriented programming concept that binds together the data and functions that manipulate the data,
and that keeps both safe from outside interference and misuse.
"""

#Private Variables
"""
Private variables can only be accessed within the class.
Private variables are defined using the double underscore '__' prefix.
"""

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def display(self):
        print(self.__name)
        print(self.__age)

p1 = Person("John", 36)

#p1.__name    #This will raise an error
p1.display()  #Output: John 36