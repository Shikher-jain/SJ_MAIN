# Python program to demonstrate
# logical and operator

a = 10
b = 10
c = -10

if a > 0 and b > 0:
    print("The numbers are greater than 0")

if a > 0 and b > 0 and c > 0:
    print("The numbers are greater than 0")
else:
    print("Atleast one number is not greater than 0")


# Python program to demonstrate
# logical and operator

a = 10
b = 12
c = 0

if a and b and c:
    print("All the numbers have boolean value as True")
else:
    print("Atleast one number has boolean value as False")


# Python program to demonstrate
# logical or operator

a = 10
b = -10
c = 0

if a > 0 or b > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")

if b > 0 or c > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")



# Python program to demonstrate
# logical and operator

a = 10
b = 12
c = 0

if a or b or c:
    print("Atleast one number has boolean value as True")
else:
    print("All the numbers have boolean value as False")



# Python program to demonstrate
# logical not operator

a = 10

if not a:
    print("Boolean value of a is True")

if not (a%3 == 0 or a%5 == 0):
    print("10 is not divisible by either 3 or 5")
else:
    print("10 is divisible by either 3 or 5")


# Python program to demonstrate
# order of evaluation of logical 
# operators

def order(x):
    print("Method called for value:", x)
    return True if x > 0 else False
    
a = order
b = order
c = order

if a(-1) or b(5) or c(10):
    print("Atleast one of the number is positive")
