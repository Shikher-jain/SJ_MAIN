# Python program to illustrate
# Finding common member in list
# using 'in' operator
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]
for item in list1:
    if item in list2:
        print("overlapping")
    else:
        print("not overlapping")


# Python program to illustrate
# Finding common member in list
# without  using 'in' operator

#  Define a function() that takes two lists


def overlapping(list1, list2):

    c = 0
    d = 0
    for i in list1:
        c += 1
    for i in list2:
        d += 1
    for i in range(0, c):
        for j in range(0, d):
            if(list1[i] == list2[j]):
                return 1
    return 0


list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]
if(overlapping(list1, list2)):
    print("overlapping")
else:
    print("not overlapping")


# Python program to illustrate
# not 'in' operator
x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is  present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")


# Python program to illustrate the use
# of 'is' identity operator
x = 5
y = 5
print(x is y)
id(x)
id(y)

# Python program to illustrate the
# use of 'is not' identity operator
x = 5
if (type(x) is not int):
    print("true")
else:
    print("false")

# Prints True
x = 5.6
if (type(x) is not int):
    print("true")
else:
    print("false")


