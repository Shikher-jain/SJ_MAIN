s1='geeksforgeeks'
s2='geeks'
print(s2 in s1)
print(s2 not in s1)

# Defining strings
var1 = "Hello "
var2 = "World"
 
# + Operator is used to combine strings
var3 = var1 + var2
print(var3)

#         012345
string = 'random'

print("index of 'and' in string:", string.index('and'))
print("index of 'and' in string:", string.index('and',1))
print("index of 'and' in string:", string.index('nd',2,5))


# initializing target string
ch = "geeksforgeeks"
 # initializing argument string
ch1 = "geeks"
pos = ch.index(ch1,2)
print("The first position of geeks after 2nd index : ",end="")
print(pos)


test_string = "1234gfg4321"
# finding gfg in string segment 'gfg4'
print(test_string.index('gfg', 4, 8))
# finding "21" in string segment 'gfg4321'
print(test_string.index("21", 8, len(test_string)))
# finding "32" in string segment 'fg432' using negative index
print(test_string.index("32", 5, -1))

word = 'geeks for geeks'
print(word.find('for'))



string = "ring ring"
# checks for the substring in the range 0-4 of the string
print(string.rindex("ring", 0, 4))
# same as using 0 & 4 as start, end value
print(string.rindex("ring", 0, -5))
string = "101001010"
# since there are no '101' substring after string[0:3]
# thus it will take the last occurrence of '101'
print(string.rindex('101', 2))


string = "ring ring"
# search for the substring,
# from right in the whole string
print(string.rindex("ring"))
string = "geeks"
# this will return the right-most 'e'
print(string.rindex('e'))
