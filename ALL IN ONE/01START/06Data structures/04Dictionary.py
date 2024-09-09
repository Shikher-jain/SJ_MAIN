Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(Dict)


# Creating a Dictionary
# with Integer Keys
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)
  
# Creating a Dictionary
# with Mixed keys
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)


# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)


# Creating a Dictionary
# with dict() method
Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict)

# Creating a Dictionary
# with each item as a Pair
Dict = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
# Creating a Nested Dictionary
# as shown in the below image
Dict = {1: 'Geeks', 2: 'For',
        3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}  
print(Dict)


# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)
# Adding elements one at a time
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)
# Adding set of values
# to a single Key
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict)  
# Updating existing Key's Value
Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)
# Adding Nested Key value to Dictionary
Dict[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
print("\nAdding a Nested Key: ")
print(Dict)


# Python program to demonstrate
# accessing a element from a Dictionary
# Creating a Dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
# accessing a element using key
print("Accessing a element using key:")
print(Dict['name'])
# accessing a element using key
print("Accessing a element using key:")
print(Dict[1])


# Creating a Dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
  
# accessing a element using get()
# method
print("Accessing a element using get:")
print(Dict.get(3))


# Creating a Dictionary
Dict = {'Dict1': {1: 'Geeks'},
        'Dict2': {'Name': 'For'}}
  
  
# Accessing element using key
print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])
# demo for all dictionary methods
dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}
# copy() method
dict2 = dict1.copy()
print(dict2)
# clear() mthod
dict1.clear()
print(dict1)
# get() method
print(dict2.get(1))
# items() method
print(dict2.items())
# keys() method
print(dict2.keys())
# pop() method
dict2.pop(4)
print(dict2)
# popitem() method
dict2.popitem()
print(dict2)
  # update() method
dict2.update({3: "Scala"})
print(dict2)
  # values() method
print(dict2.values())


"""
Dictionary methods
======================

clear()     –~-~-~-~-~->   Remove all the elements from the dictionary
pop()       –~-~-~-~-~->   Remove the element with specified key
popitem()   –~-~-~-~-~->   Removes the last inserted key-value pair
copy()      –~-~-~-~-~->   Returns a copy of the dictionary
get()       –~-~-~-~-~->   Returns the value of specified key
items()     –~-~-~-~-~->   Returns a list containing a tuple for each key value pair
keys()      –~-~-~-~-~->   Returns a list containing dictionary’s keys
values()    –~-~-~-~-~->   Returns a list of all the values of dictionary
update()    –~-~-~-~-~->   Updates dictionary with specified key-value pairs
"""