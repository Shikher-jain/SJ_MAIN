# a=input()
# b=input()
# print(a+b)

# def main():
#     return 0

# if __name__ == '__main__':
#     main()
#     A=int(input())
#     B=int(input())
#     C=int(input())
#     D=int(input())
#     E=int(input())

#     F=format((A+B+C+D+E)/5,".2f")
#     print(F)

# N=input()
# print(f"Hello {N}")

# A=int(input())
# B=int(input())
# print( A+B, A*B, A-B, A//B)

# A=input()
# B=input()
# print(f"{A} says Hi to {B}")

# print("A\nB\nC\nD\nE")

# A=int(input())
# for i in range(1,11):
#     print(f"{A} * {i} = ",A*i)

# for i in range(1,int(input())+1):
#     print(i,end=" ")

# for i in range(int(input()),0,-1):
#     print(i,end=" ")

# T=[]
# N=int(input())
# for i in range(N):
#     T.append(input())
# for i in T:
#     # print(i)
#     print(i[0],i[-1])

# N=int(input())
# for n in range(2,N+1):
#     f=0
#     for i in range(2,n//2+1):
#         if(n%i==0):
#             f=1
#             break
#     if (f==0):
#        print(n)
    
# N = 20
# for n in range(2, N + 1):
#     is_prime = True
#     for i in range(2, n // 2 + 1):
#         if n % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(n)

# N=int(input())
# f=0
# for i in range(2,N//2+1):
#     if(N%i==0):
#         f=1
#         break    
# if f==0:
#     print("YES")
# else:print("NO")

# N=int(input())
# T=[]
# for i in range(N):
#     T.append(input())
# for j in range(N):
#     print(len(T[j]))

# T=int(input("Test case"))
# # N=[10,81,84,94,50,39,6,39,83,8,73]
# s=0
# for i in range(T):
#     N.append(int(input()))
# for i in range(len(N)):
#     for n in range(1,N[i]+1):
#         s+=1
#     # print("s = ",s)
#     if (N[i]%s==0):
#         print("YES")
#     else:print("NO")
# # print(N)

# def is_perfect_number(n):
#     # If n is less than or equal to 1, it cannot be a perfect number
#     if n <= 1:
#         return "NO"
#     # Calculate the sum of proper divisors
#     sum_of_divisors = 0
#     for i in range(1, n // 2 + 1):
#         if n % i == 0:
#             sum_of_divisors += i
#     # Check if sum of divisors is equal to n
#     return sum_of_divisors == n
# def main():
#     T = int(input("Enter the number of test cases: "))
#     results = []
#     for _ in range(T):
#         N = int(input("Enter a number: "))
#         if is_perfect_number(N):
#             results.append("YES")
#         else:
#             results.append("NO")
#     # Print all results
#     for result in results:
#         print(result)
#     main()

# A=input()  # Enter no. to check pal lindrone
# if int(A)<0:
#     print(0)
# else:
#     if A==A[::-1]:
#         print(True)
#     else:
#         print(False)

# print('\u20b9')

# print("\\")

# print("SHIKHER".zfill(9))

# for i in range(1,11):
#     print(i)
# else:
#     print(-1)

# t=int(input("Enter no. : ").strip())
# print(t)
# t=int(input("Enter no. : "))
# print(t)

# move="8"
# move+"a"
# move+"b"
# move+"c"
# print(move)

# t = int(input().strip())
# for _ in range(t):
#     m = []
#     n = int(input().strip())
#     for i in range(n):
#         m.append(list(map(int, input(f"i:{i+1},m{m}").strip().split())))
#         print(m)
# print(m)

# n=10
# lst = list(map(int, input(
#     "Enter the integer elements of list(Space-Separated): ").strip().split()))[:n]
# print('The list is:', lst) 

# name = raw_input("Enter your name: ")  #python 2
# print("Hello, " + name)

# name = input("Enter your name: ")  #python 3
# print("Hello, " + name)

# exp = input("Enter your exp: ")  
# print("EXPRESSION : " + exp)

# exp = eval(input("Enter your exp: "))
# print("EXPRESSION : " + str(exp))

# print(1//+1.0/2)

# s=10
# for i in range(s):
            
#         if i==0 or i==s-1:
#             for j in range(s):
#                 print("*",end=" ")
            
#         elif i>0 or i<s-1 :
#             print("*",end=" ")
#             for _ in range(s-2):
#                 print(" ",end=" ")
#             print("*",end=" ")
            
#         else:
#             print("o")
#         print()

# s=4
# for i in range(s):
#     for _ in range(s):
#         print("*",end=" ")
#     print()


# s=4       
# for i in range(s):
#         print("* "*s)
    
# s=5
# for i in range(1,s+1):
    
#     print("* "*i)

# s=8
# for i in range(s):
#     if i == 0 :
#         print("*",end=" ")
        
#         # ..............
        
#     elif s-1> i > 0:
#         print("*",end="")
#         for _ in range(i):
#             print(" ",end=" ")
#         print("*",end=" ")
#         # .................
        
        
#     else:
#         # ...............
#         print("* "*s)
#     print()


# ss=''' 
# *
# *  *
# *    *
# *      *
# *        *
# *          *
# *            *
# *              *
# * * * * * * * * *'''

# # Expected Output: 
# sss='''
# *
# *  *
# *    *
# *      *
# *        *
# *          *
# *            *
# *              *
# * * * * * * * * *'''

# if ss==sss:
#     print("yes")
# else:
#     print("no")

# n = 5  # Number of rows
# print("*")
# for i in range(2, n):
#     print("*" + "  " * (i-1) + "*")
# print("* " * n)  # Bottom row of asterisks


# n = 5  # Number of rows

# for i in range(1, n + 1):
#     if i == 1 or i == n:
#         print("* " * i)  # Print the full line for the first and last rows
#     else:
#         print("*" + "  " * (i - 2) + " *")  # Print a star, followed by spaces, and then another star


# n = 5  # Number of rows

# for i in range(n, 0, -1):
    # print("* " * i)


# s=5
# for j in range(s,0,-1):
#     for i in range(j):
#         print("*",end=" ")
#     print()


# n=10
# ans = 0
# for i in range(n+1):
#     ans+=i
# print( ans)


# print(5%20)

# print((4+5)*5**(4-2));

# str = "GFG"
# print(not (not(str and "")))
# print(not(str and ""))

# s = "gfg"
# print("G" in s)

# s = "gfg"
# print(("g" or "") in s)

# s = "gfg"
# print(not ("g" or "") not in s)

# print(oct(23))

# print(oct(23)+oct(23))

# print(~(~2))

# str=""
# str[2]="w"
# print(str)

# print(max("geeksforgeeks")) #ASCII VALUE 

# print("ss"+"ww")
# print("ss".__add__("ww"))

# a,b=1,2,3

import sys


print(len("abc"))
print(sys.getsizeof("abc"))