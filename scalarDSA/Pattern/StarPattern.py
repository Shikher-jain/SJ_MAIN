# N=int(input("Enter how many Syars you wants to print: "))
# for i in range(N):                                              #* * * * * * * *  R=8
#     print("*",end=" ")

# R=int(input("Enter how many Rows you wants to print: "))        #|* * * * *   R=5
# for i in range(R):                                              #|* * * *
#     for j in range(R-i):                                        #|* * *
#         print("*",end=" ")                                      #|* * 
#     print()                                                     #|*


# R=int(input("Enter how many Rows you wants to print: "))        #|* * * * *           R=5
# for i in range(R):                                              #|* * * * * 
#     for j in range(R):                                          #|* * * * * 
#         print("*",end="")                                       #|* * * * * 
#     print()                                                     #|* * * * * 

# R=int(input())
# C=int(input())
# for i in range(R):
#     for j in range(C):
#         print("*",end="")
#     print()

# R=int(input("Enter how many Rows you wants to print: "))        #|*           R=5
# for i in range(R):                                              #|* *
#     for j in range(i+1):                                        #|* * *
#         print("*",end=" ")                                      #|* * * * 
#     print()                                                     #|* * * * *


# R=int(input("Enter how many Rows you wants to print: "))        #|            *  R=7
# for i in range(1,R+1):                                          #|          * *
#     for j in range(R-i):                                        #|        * * *
#         print(" ",end=" ")                                      #|      * * * * 
#     for k in range(i):                                          #|    * * * * *
#         print("*",end=" ")                                      #|  * * * * * *
#     print()                                                     #|* * * * * * *


# R=int(input("Enter how many Rows you wants to print: "))        #|* * * * * * *    R=7
# for i in range(R):                                              #|  * * * * * *
#     for j in range(i):                                          #|    * * * * *
#         print(" ",end=" ")                                      #|      * * * *
#     for k in range(R-i):                                        #|        * * *
#         print("*",end=" ")                                      #|          * *        
#     print()                                                     #|            *


# R=int(input("Enter how many Rows you wants to print: "))      
# for i in range(1,R+1):                                        
#     for j in range(R-i):                   #|   R=6      
#         print(" ",end=" ")                 #|          * 
#     for k in range(i):                     #|        * * *
#         print("*",end=" ")                 #|      * * * * *    
#     for l in range(i-1):                   #|    * * * * * * *
#         print("*",end=" ")                 #|  * * * * * * * * *
#     print()                                #|* * * * * * * * * * *


# R=int(input("Enter the size of square which you wants to print: "))
# R=4
# for i in range(R):
#     for j in range(0,R-i):
#         # print("*",end="")
#         print(i,j,end=",")
#         if i+j==R:
#             print("o",end="")
#     print()


# R=4
# for i in range(R):
#     for j in range(0,R-i):
#         print("*",end=" ")                         #|  * * * * * *
#     for k in range(i):                             #|    * * * * *
#         print(" ",end=" ")                         #|      * * * *
#         print(" ",end=" ")                         #|      * * * *
#     for l in range(R-i):                           #|        * * *
#         print("*",end=" ")                         #|          * *        

#     print()


num_rows = int(input())
for i in range(num_rows):
    num_stars = num_rows - i  # Number of stars on each side
    num_spaces = 2 * i        # Number of underscores in the middle
    stars = '* ' * num_stars
    spaces = '  ' * num_spaces
    pattern = stars + spaces + stars
    
    print(pattern)


# R=int(input("Enter how many Rows you wants to print: "))        
# for i in range(1,R+1):                          #|*                   * 
#     for j in range(i):                          #|* *               * * 
#         print("*",end=" ")                      #|* * *           * * *    R=6
#     # for k in range(R-i):                      #|* * * *       * * * * 
#     for k in range(2*(R-i)):                    #|* * * * *   * * * * * 
#         print(" ",end=" ")                      #|* * * * * * * * * * * 
#     # for k in range(R-i):                                    
#         # print(" ",end=" ")                                    
#     for l in range(i):                                         
#         print("*",end=" ")                                      
#     print()                                                  


# R=int(input("Enter how many Rows you wants to print: "))
# for i in range(R):
#     for j in range(i):                  # | | | | | 
#         print(" ", end="")              #  | | | |
#     for j in range(i, R):               #   | | |
#         print("| ", end="")             #    | |
#     print()                             #     |
    

# R=int(input("Enter how many Rows you wants to print: "))
# for i in range(1,R+1):                    #     | 
#     for j in range(R-i):                  #    | |
#         print(" ", end="")                #   | | |
#     for j in range(i,0,-1):               #  | | | |
#         print("| ", end="")               # | | | | |
#     print()


# R=int(input("Enter how many Rows you wants to print: "))
# for i in range(R):
#     for j in range(R, i, -1):           #      * 
#         print(" ", end="")              #     * *
#     for k in range(i + 1):              #    * * *
#         print("* ", end="")             #   * * * *
#     print()                             #  * * * * *


# R=int(input("Enter how many Rows you wants to print: "))
# k=1
# for i in range(1,1+R):          # 1 
#     for j in range(i):          # 2 3
#         print(k,end=" ")        # 4 5 6
#         k+=1                    # 7 8 9 10
#     print()                     # 11 12 13 14 15


# R=int(input("Enter how many Rows you wants to print: "))
# for i in range(1,1+R):          # 1 
#     k=1                         # 1 2 
#     for j in range(i):          # 1 2 3 
#         print(k,end=" ")        # 1 2 3 4 
#         k+=1                    # 1 2 3 4 5 
#     print()

#end with no space
# R=int(input("Enter how many Rows you wants to print: "))
# for i in range(1,1+R):                           # 1
#     k=1                                          # 1 2
#     for j in range(i):                           # 1 2 3
#         print(k,end="" if k==i else " ")         # 1 2 3 4
#         k+=1                                     # 1 2 3 4 5
#     print()

# R=int(input("ROWS: "))
# # print(1,end="")
# for i in range(1,1+R):                 # 1
#     k=1                                # 1_ 
#     for j in range(0,i,2):             # 1_3 
#         if k==i:                       # 1_3_
#             print(k,end="")            # 1_3_5
#         else:                          
#             print(k,end=" ")
#         k+=2                           
#     print()

# R=int(input("Enter the size of square which you wants to print: "))
# for i in range(R):
#     print("*",end=" ")
# print()
# for j in range(R-2):                        # * * * * * *
#     print("*",end=" ")                      # *         *
#     for j in range(R-2):                    # *         *
#         print(" ",end=" ")                  # *         *
#     print("*")                              # *         *
# for i in range(R):                          # * * * * * *
#     print("*",end=" ")      

# R=int(input("Enter the size of square which you wants to print: "))
# for j in range(R):                        
#     print("*",end="")                      # *    *   R=4
#     for j in range(R-2):                   # *    *    space -> R-2
#         print(" ",end="")                  # *    *
#     print("*")                             # *    *
    # print()