# Using list comprehension to iterate through loop
List = [character for character in [1, 2, 3]]
# Displaying list
print(List)


list = [i for i in range(11) if i % 2 == 0]
print(list)


matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)


# Empty list
List = [] 
# Traditional approach of iterating
for character in 'Geeks 4 Geeks!':
    List.append(character)
# Display list
print(List)


# Using list comprehension to iterate through loop
List = [character for character in 'Geeks 4 Geeks!'] 
# Displaying list
print(List)



# Python code to demonstrate dictionary
# comprehension
# Lists to represent keys and values
keys = ['a','b','c','d','e']
values = [1,2,3,4,5] 
# but this line shows dict comprehension here 
myDict = { k:v for (k,v) in zip(keys, values)} 
# We can use below too
# myDict = dict(zip(keys, values))  
print (myDict)
