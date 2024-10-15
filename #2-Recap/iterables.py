#A recap of python collection arrays / iterables, (lists, tuples, sets, dictionaries)

#Lists
"""
Lists store multiple items in a single variable
Lists are characterized by square brackets []
Lists are ordered, malleable and allow duplicate values
List items are indexed, starting from 0
List items can be of different data types
"""

#Creating a list
firstList = ["BMW", "Mercedes", "Audi", "Porsche"]
print(firstList)

#List with duplicate values
secondList = ["Mango, Orange, Banana, Apple, Mango"]
print(secondList)

#Accessing items in a list
thirdList = [1, "Africa", 3.0, "South America", True]
print(thirdList[2])     #prints 3.0 (Third item)
print(thirdList[-2])    #prints South America (Second last item)
print(thirdList[1:3])   #prints ['Africa', 3.0] (Second to third item)
print(thirdList[:3])    #prints [1, 'Africa', 3.0] (First to third item)
print(thirdList[1:])    #prints ['Africa', 3.0, 'South America', True] (Second to last item)
print(thirdList[-4:-1]) #prints ['Africa', 3.0, 'South America'] (Searches backwards from the third item)

#Changing list items
fourthList = ["Fanta, Sprite, Coca-cola, Blackcurrant, Stoney, Krest"]
fourthList[2] = "Juice"                         #Replaces the third item with Juice
fourthList[1:3] = ["Pepsi, Schweppes, Water"]   #Replaces items in a range
print(fourthList)

#Inserting & appending items
fifthList = ["School, Hospital, Office, Golf Course"]
fifthList.insert(2, "Apartment")                            #At the third index, insert 'Apartment'
fifthList.insert(0, "Mall")                                 #At the first index, insert 'Mall'
fifthList.append("Playground")                              #Add 'Playground' after the last list item
print(fifthList)

#Extending lists
sixthList = ["Park, City Hall, Parliament"]
fifthList.extend(sixthList)                                 #To the fifthList, add items from sixthList
print(fifthList)

#Removing items
seventhList = [25, 33.7, 44, False, "Seventh List"]
seventhList.remove(25)                                      #Remove list item 25
seventhList.pop(2)                                          #Remove third list item
seventhList.pop()                                           #Remove last item
seventhList.clear()                                         #Clear the list
del seventhList[1]                                          #Remove second item
del seventhList                                             #Delete the entire list
print(seventhList)

#Looping lists
eighthList = ["French, Spanish, English, Swahili, Japanese, Portugese"]
for x in eighthList:
    print(x)                                                #Looping the list

for i in range(len(eighthList)):
    print(eighthList[i])                                    #Looping through indexes

while i < len(eighthList):
    print(eighthList[i])                                    #Looping using while loop
    i = i+1

[print(x) for x in eighthList]                              #Looping using list comprehension

#List comprehension
ninthList = ["Nairobi, New York, Delhi, Madrid, Brazil, Sydney"]
newlist = [x for x in ninthList if "J" in x]                    #[expression for item in iterable if condition == True]
newlist = [x if x != "Delhi" else "Tokyo" for x in ninthList]   #Return Tokyo instead of Delhi
print(newlist)

#Sorting a list
tenthList = ["Green, Red, White, Pink, Yellow, Purple, Cream"]
tenthList.sort()                                            #Sort in ascending order
tenthList.sort(reverse=True)                                #Sort in descending order
tenthList.sort(key=str.lower)                               #Sort without case-insensitivity
tenthList.reverse()                                         #Reverse order regardless of alphabet
print(tenthList)

#Copying a list
eleventhList = tenthList.copy()                             #Copy with copy method
eleventhList = list(tenthList)                              #Copy with list keyword
eleventhList = tenthList[:]                                 #Copy with slice operator
print(eleventhList)

#Joining lists
twelvethList = eleventhList + tenthList + ninthList         #Joining lists using concatenator

for x in eleventhList:                                      #Joining using append method
    twelvethList.append(x)
print (twelvethList)

twelvethList.extend(eleventhList)                           #Joining using extend method
print(twelvethList)

#Summary
"""
append()    Adds items to the end of the list
clear()     Removes all items from the list
copy()      Returns a copy of the list
count()     Returns the number of items  in the list
extend()    Add items from any other collection/iterable to the end of the list
index()     Returns the index of first item in specified value
insert()    Adds item in specified index
pop()       Removes item in specified index
remove()    Removes item in specified value/index
sort()      Sorts the list
"""

#Tuples
"""
Tuples store multiple items in a single variable
Tuples are characterized by round brackets ()
Tuples are ordered, unchangeable and allow duplicate values
Tuple items are indexed, starting from 0
Tuple items can be of different data types
"""

#Creating a tuple
firstTuple = ("BMW", "Mercedes", "Audi", "Porsche")

#Accessing items in a tuple
print(firstTuple[2])     #prints Audi (Third item)
print(firstTuple[-2])    #prints Audi (Second last item)

#Changing tuple items
firstTuple[2] = "Toyota"           #Returns an error since tuples are unchangeable
"""
NOTE: Tuples are unchangeable
It requires conversion to a list, change the list, then convert back to a tuple
This is the same for appending, removing, inserting, etc.
"""

#Looping tuples
for x in firstTuple:
    print(x)                        #Looping the tuple

#Packing and unpacking tuples
secondTuple = ("Europe", "Asia", "Africa", "America")
(first, second, third, fourth) = secondTuple
print(first)                        #prints Europe
print(second)                       #prints Asia
print(third)                        #prints Africa
print(fourth)                       #prints America

#Joining and multiplying tuples
thirdTuple = firstTuple + secondTuple
print(thirdTuple)                   #Joins the two tuples

fourthTuple = firstTuple * 2
print(fourthTuple)                  #Duplicates the firstTuple


#Tuple methods
"""
count()     Returns the number of times a specified value occurs in a tuple
index()     Searches the tuple for a specified value and returns the position of where it was found
"""

#Sets
"""
Sets store multiple items in a single variable
Sets are characterized by curly brackets {}
Sets are NOT ordered, NOT indexed and DO NOT allow duplicate values
Set items can be of different data types
"""

#Creating a set
firstSet = {"BMW", "Mercedes", "Audi", "Porsche"}
print(firstSet)

#Accessing items in a set
for x in firstSet:
    print(x)                        #Looping the set

#Adding items to a set
firstSet.add("Toyota")
print(firstSet)

#Updating a set
firstSet.update(["Ford", "Nissan", "Honda"])

secondSet = {"GMC, Caddilac, Chevrolet, Dodge"}
firstSet.update(secondSet)           #Adds items from secondSet to firstSet
"""
NOTE: The update() method can take any iterable(list, set, dictionary, tuple) as an argument
"""

#Removing items from a set
firstSet.remove("Ford")             #Removes specified item
firstSet.discard("Nissan")          #Removes specified item
firstSet.pop()                      #Removes last item
firstSet.clear()                    #Clears the set
del firstSet                        #Deletes the set

#Joining sets
secondSet = {"GMC, Caddilac, Chevrolet, Dodge"}
thirdSet = firstSet.union(secondSet) #Joins two sets
print(thirdSet)

#Set methods
"""
add()                           Adds an item to the set
clear()                         Removes all items from the set
copy()                          Returns a copy of the set
difference()                    Returns a set containing the difference between two or more sets
difference_update()             Removes the items in this set that are also included in another, specified set
discard()                       Removes the specified item
intersection()                  Returns a set containing the intersection of two or more sets
intersection_update()           Removes the items in this set that are not present in other, specified set(s)
isdisjoint()                    Returns whether two sets have a intersection or not
issubset()                      Returns whether another set contains this set or not
issuperset()                    Returns whether this set contains another set or not
pop()                           Removes an element from the set
remove()                        Removes the specified element
symmetric_difference()          Returns a set with the symmetric differences of two sets
symmetric_difference_update()   Inserts the symmetric differences from this set and another
union()                         Return a set containing the union of sets
update()                        Update the set with the union of this set and others
"""

#Dictionary
"""
Dictionaries store multiple items in a single variable
Dictionaries are characterized by curly brackets {}
Dictionaries are ordered in latest python versions, changeable and DO NOT allow duplicate values
Dictionary items are indexed, starting from 0
Dictionary items can be of different data types
"""

#Creating a dictionary
firstDict = {
    "brand": "BMW",
    "model": "X5",
    "year": 2020
}

#Accessing items in a dictionary
print(firstDict["model"])           #prints X5 (Model key)
print(firstDict.get("year"))        #prints 2020 (Year key)

#Changing dictionary items
firstDict["year"] = 2021            #Changes the year value
firstDict.update({"color": "Black"})#Adds a new key-value pair
print(firstDict)

#Looping dictionaries
for x in firstDict:
    print(x)                        #Looping the dictionary keys

for x in firstDict:
    print(firstDict[x])             #Looping the dictionary values

for x in firstDict.values():
    print(x)                        #Looping the dictionary values

for x, y in firstDict.items():
    print(x, y)                     #Looping the dictionary keys and values

#Copying a dictionary
secondDict = firstDict.copy()       #Copies the dictionary
secondDict = dict(firstDict)        #Copies the dictionary
print(secondDict)

#Nested dictionaries
thirdDict = {
    "child1": {
        "name": "John",
        "age": 12
    },
    "child2": {
        "name": "Jane",
        "age": 10
    },
    "child3": {
        "name": "Doe",
        "age": 8
    }
}

#Dictionary methods
"""
clear()     Removes all items from the dictionary
copy()      Returns a copy of the dictionary
fromkeys()  Returns a dictionary with specified keys and values
get()       Returns the value of the specified key
items()     Returns a list of key-value pairs
keys()      Returns a list of keys
pop()       Removes the specified key
popitem()   Removes the last inserted key-value pair
setdefault()Returns the value of the specified key. If the key does not exist, insert the key with the specified value
update()    Updates the dictionary with the specified key-value pairs
values()    Returns a list of values
"""

#Summary
"""
Lists       Ordered, malleable, allows duplicate values
Tuples      Ordered, unchangeable, allows duplicate values
Sets        Unordered, unindexed, does not allow duplicate values
DictionariesOrdered, changeable, does not allow duplicate values
"""