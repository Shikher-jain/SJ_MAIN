
R=int(input("Enter the size of square which you wants to print: "))
for i in range(R):
    print("*",end=" ")
print()
for j in range(R-2):                        # * * * * * *
    print("*",end=" ")                      # *         *
    for j in range(R-2):                    # *         *
        print(" ",end=" ")                  # *         *
    print("*")                              # *         *
for i in range(R):                          # * * * * * *
    print("*",end=" ")      
