Var = ["Geeks", "for", "Geeks"]
print(Var)


# Python program to demonstrate
# Creation of List
 
# Creating a List
List = []
print("Blank List: ")
print(List)
 
# Creating a List of numbers
List = [10, 20, 14]
print("\nList of numbers: ")
print(List)
 
# Creating a List of strings and accessing
# using index
List = ["Geeks", "For", "Geeks"]
print("\nList Items: ")
print(List[0])
print(List[2])


# Python program to demonstrate
# accessing of element from list
 
# Creating a List with
# the use of multiple values
List = ["Geeks", "For", "Geeks"]
 
# accessing a element from the
# list using index number
print("Accessing a element from the list")
print(List[0])
print(List[2])


# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = [['Geeks', 'For'], ['Geeks']]
 
# accessing an element from the
# Multi-Dimensional List using
# index number
print("Accessing a element from a Multi-Dimensional list")
print(List[0][1])
print(List[1][0])


List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
 
# accessing an element using
# negative indexing
print("Accessing element using negative indexing")
 
# print the last element of list
print(List[-1])
 
# print the third last element of list
print(List[-3])


# Creating a List
List1 = []
print(len(List1))
 
# Creating a List of numbers
List2 = [10, 20, 14]
print(len(List2))


# Python program to demonstrate
# Addition of elements in a List
 
# Creating a List
List = []
print("Initial blank List: ")
print(List)
 
# Addition of Elements
# in the List
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)
 
# Adding elements to the List
# using Iterator
for i in range(1, 4):
    List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)
 
# Adding Tuples to the List
List.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List)
 
# Addition of List to a List
List2 = ['For', 'Geeks']
List.append(List2)
print("\nList after Addition of a List: ")
print(List)


lis = ['Geeks', 'Geeks']
lis.insert(1, "For")
print(lis)


list1 = [ 1, 2, 3, 4, 5, 6, 7 ] 
  # insert 10 at 4th index 
list1.insert(4, 10) 
print(list1) 


list2 = ['a', 'a', 'a', 'b', 'b', 'a', 'c', 'b']
print(list2.count('b'))


# program to demonstrate use of del keyword
# assign list
numbers = [1, 2, 3, 2, 3, 4, 5]
# use del
del numbers[2]
# display list
print(numbers)
# use del
del numbers[-1]
# display list
print(numbers)
# use del
del numbers[0]
# display list
print(numbers)



# program to demonstrate use of remove() metho
# assign list
numbers = [1, 2, 3, 2, 3, 4, 5]
# use remove()
numbers.remove(3)
# display list
print(numbers)
# use remove()
numbers.remove(2)
# display list
print(numbers)
  # use remove()
numbers.remove(5)
  # display list
print(numbers)



# program to demonstrate use of pop() method
# assign list
numbers = [1, 2, 3, 2, 3, 4, 5]
# use remove()
numbers.pop(3)
# display list
print(numbers)
# use remove()
numbers.pop(-1)
# display list
print(numbers)
# use remove()
numbers.pop(0)
  # display list
print(numbers)


# Python code to demonstrate the working of
# max()
# printing the maximum of 4,12,43.3,19,100
print("Maximum of 4,12,43.3,19 and 100 is : ",end="")
print (max( 4,12,43.3,19,100 ) )


# Python code to demonstrate the working of
# min()
 # printing the minimum of 4,12,43.3,19,100
print("Minimum of 4,12,43.3,19 and 100 is : ",end="")
print (min( 4,12,43.3,19,100 ) )


# Python program to demonestrate to
# sorting numbers in Ascending Order  
numbers = [1, 3, 4, 2]
# Sorting list of Integers in ascending
numbers.sort()
print(numbers)


# Python3 program to demonstrate the
# use of reverse method
# a list of numbers
list1 = [1, 2, 3, 4, 1, 2, 6]
list1.reverse()
print(list1)
# a list of characters
list2 = ['a', 'b', 'c', 'd', 'a', 'a']
list2.reverse()
print(list2) 


