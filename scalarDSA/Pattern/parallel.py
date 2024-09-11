
R=int(input("Enter the size of square which you wants to print: "))
for j in range(R):                        
    print("*",end="")                      # *    *   R=4
    for j in range(R-2):                   # *    *    space -> R-2
        print(" ",end="")                  # *    *
    print("*")                             # *    *
    print()