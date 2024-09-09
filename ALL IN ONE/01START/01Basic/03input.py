# Python program showing 
# a use of input()
  
val = input("Enter your value: ")
print(val)


name = input('What is your name?\n')     # \n ---> newline  ---> It causes a line break
print(name)

# Program to check input 
# type in Python
  
num = input ("Enter number :")
print(num)
name1 = input("Enter name : ")
print(name1)
  
# Printing type of input value
print ("type of number", type(num))
print ("type of name", type(name1))


# take input from user
input_a = input()
 
# print data type
print(type(input_a))
 
# type cast into integer
input_a = int(input_a)
 
# print data type
print(type(input_a))


# string input
input_a = input()
 
# print type
print(type(input_a))
 
# integer input
input_b = int(input())
 
# print type
print(type(input_b))


# Python program to take integer input  in Python
 
# input size of the list
n = int(input("Enter the size of list : "))
# store integers in a list using map, split and strip functions
lst = list(map(int, input(
    "Enter the integer elements of list(Space-Separated): ").strip().split()))[:n]
print('The list is:', lst)   # printing the list
