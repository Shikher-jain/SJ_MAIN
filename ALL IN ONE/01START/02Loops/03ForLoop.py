# Python program to illustrate
# Iterating over a list
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)


# Iterating over dictionary
print("Dictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345

for i in d:
    print("%s %d" % (i,d[i]))
for i in d:
    print(f"{i} -> {d[i]}")


# Iterating over a String
print("String Iteration")
s = "Geeks"
for i in s:
    print(i)
