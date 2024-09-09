var = {"Geeks", "for", "Geeks"}
print(type(var))


# typecasting list to set
myset = set(["a", "b", "c"])
print(myset) 
# Adding element to the set
myset.add("d")
print(myset)


# Python program to demonstrate differences
# between normal and frozen set
# Same as {"a", "b","c"}
normal_set = set(["a", "b","c"]) 
print("Normal Set")
print(normal_set)
# A frozen set
frozen_set = frozenset(["e", "f", "g"])
print("\nFrozen Set")
print(frozen_set)
# Uncommenting below line would cause error as
# we are trying to add element to a frozen set
# frozen_set.add("h")


# A Python program to
# demonstrate adding elements
# in a set
# Creating a Set
people = {"Jay", "Idrish", "Archi"}
print("People:", end = " ")
print(people)
# This will add Daxit
# in the set
people.add("Daxit")
# Adding elements to the
# set using iterator
for i in range(1, 6):
    people.add(i) 
print("\nSet after adding element:", end = " ")
print(people)


# Python Program to
# demonstrate union of
# two sets
 
people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
dracula = {"Deepanshu", "Raju"}
 
# Union using union()
# function
population = people.union(vampires)
 
print("Union using union() function")
print(population)
 
# Union using "|"
# operator
population = people|dracula
 
print("\nUnion using '|' operator")
print(population)


# Python program to
# demonstrate intersection
# of two sets
 
set1 = set()
set2 = set()
 
for i in range(5):
    set1.add(i)
 
for i in range(3,9):
    set2.add(i)
 
# Intersection using
# intersection() function
set3 = set1.intersection(set2)
 
print("Intersection using intersection() function")
print(set3)
 
# Intersection using
# "&" operator
set3 = set1 & set2
 
print("\nIntersection using '&' operator")
print(set3)


# Python program to
# demonstrate difference
# of two sets
 
set1 = set()
set2 = set()
 
for i in range(5):
    set1.add(i)
 
for i in range(3,9):
    set2.add(i)
 
# Difference of two sets
# using difference() function
set3 = set1.difference(set2)
 
print(" Difference of two sets using difference() function")
print(set3)
 
# Difference of two sets
# using '-' operator
set3 = set1 - set2
 
print("\nDifference of two sets using '-' operator")
print(set3)



# Python program to
# demonstrate clearing
# of set
 
set1 = {1,2,3,4,5,6}
 
print("Initial set")
print(set1)
 
# This method will remove
# all the elements of the set
set1.clear()
 
print("\nSet after using clear() function")
print(set1)

'''
Operators	                Notes
==========================================
key in s	    ~~~~~~~~~~~>      containment check
key not in s	~~~~~~~~~~~>       non-containment check
s1 == s2	    ~~~~~~~~~~~>       s1 is equivalent to s2
s1 != s2	    ~~~~~~~~~~~>       s1 is not equivalent to s2
s1 <= s2	    ~~~~~~~~~~~>       s1 is subset of s2
s1 < s2	        ~~~~~~~~~~~>       s1 is proper subset of s2
s1 >= s2	    ~~~~~~~~~~~>       s1 is superset of s2
s1 > s2         ~~~~~~~~~~~>   	s1 is proper superset of s2
s1 | s2	        ~~~~~~~~~~~>       the union of s1 and s2
s1 & s2	        ~~~~~~~~~~~>       the intersection of s1 and s2
s1 – s2	        ~~~~~~~~~~~>       the set of elements in s1 but not s2
s1 ˆ s2	        ~~~~~~~~~~~>       the set of elements in precisely one of s1 or s2
'''
