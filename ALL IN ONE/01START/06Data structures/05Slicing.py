# declaring the string
str ="Geeks for Geeks !"
 
# slicing using indexing sequence
print(str[: 3])
print(str[1 : 5 : 2])
print(str[-1 : -12 : -2])


# Initialize list
Lst = [50, 70, 30, 20, 90, 10, 50]
 
# Display list
print(Lst[1:5])


tup = (22, 3, 45, 4, 2.4, 2, 56, 890, 1)
print(tup[1:4])


l1 = [10,20,30]
l2 = l1[:]
t1 = (10,20,30)
t2 = t1[:]          # tuple having same element has same id
s1 = "geeks"
s2 = s1[:]          # string of same value have same id
print(l1 is l2)
print(t1 is t2)
print(s1 is s2)


