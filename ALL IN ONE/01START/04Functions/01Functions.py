# A simple Python function
 
def fun():
  print("Welcome to GFG")



# A simple Python function
def fun():
    print("Welcome to GFG")
 
 
# Driver code to call a function
fun()

# some more functions
def is_prime(n):
    if n in [2, 3]:
        return True
    if (n == 1) or (n % 2 == 0):
        return False
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
    return True

print(is_prime(78), is_prime(79))



 
def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
# Driver code to call the function
evenOdd(2)
evenOdd(3)


# Python program to demonstrate
# default arguments
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)
 # Driver code (We call myFun() with only
# argument)
myFun(10)


# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)
# Keyword arguments
student(firstname='Geeks', lastname='Practice')
student(lastname='Practice', firstname='Geeks')


# Python program to illustrate
# *args for variable number of arguments
def myFun(*argv):
    for arg in argv:
        print(arg)
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


# A simple Python function to check
# whether x is even or odd
def evenOdd(x):
    """Function to check if the number is even or odd"""
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
# Driver code to call the function
print(evenOdd.__doc__)



def square_value(num):
    """This function returns the square
    value of the entered number"""
    return num**2
print(square_value(2))
print(square_value(-4))



# Here x is a new reference to same list lst
def myFun(x):
    x[0] = 20
# Driver Code (Note that lst is modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)


def A():
    print("hii")
print(A())

