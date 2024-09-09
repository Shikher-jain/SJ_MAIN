# Python3 program to show the
# working of upper() function
text = 'geeKs For geEkS'
# upper() function to convert
# string to upper case
print("\nConverted String:")
print(text.upper())
# lower() function to convert
# string to lower case
print("\nConverted String:")
print(text.lower())
# converts the first character to
# upper case and rest to lower case
print("\nConverted String:")
print(text.title())
# original string never changes
print("\nOriginal String")
print(text)


# Python code to implement startswith()
# and endswith() function.
  
str = "GeeksforGeeks"
  
# startswith()
print(str.startswith("Geeks"))
print(str.startswith("Geeks", 4, 10))
print(str.startswith("Geeks", 8, 14))  
print("\n")
# endswith
print(str.endswith("Geeks"))
print(str.endswith("Geeks", 2, 8))
print(str.endswith("for", 5, 8))


# Python code
# to split and join given string 
# input string
s = 'Geeks for Geeks'
# print the string after split method
print(s.split(" "))
# print the string after join method
print("-".join(s.split()))
 


# Python code to demonstrate working of 
# strip(), lstrip() and rstrip()
str = "---geeksforgeeks---"
# using strip() to delete all '-'
print ( " String after stripping all '-' is : ", end="")
print ( str.strip('-') )  
# using lstrip() to delete all trailing '-'
print ( " String after stripping all leading '-' is : ", end="")
print ( str.lstrip('-') )
# using rstrip() to delete all leading '-'
print ( " String after stripping all trailing '-' is : ", end="")
print ( str.rstrip('-') )


word = 'geeks for geeks'
print(word.find('for'))
# returns first occurrence of Substring
result = word.find('geeks')
print("Substring 'geeks' found at index:", result) 
result = word.find('for')
print("Substring 'for ' found at index:", result)
# How to use find()
if word.find('pawan') != -1:
    print("Contains given substring ")
else:
    print("Doesn't contains given substring")


word = 'geeks for geeks'
# Substring is searched in 'eks for geeks'
print(word.find('ge', 2))
# Substring is searched in 'eks for geeks'
print(word.find('geeks ', 2)) 
# Substring is searched in 's for g'
print(word.find('g', 4, 10))
# Substring is searched in 's for g'
print(word.find('for ', 4, 11))
