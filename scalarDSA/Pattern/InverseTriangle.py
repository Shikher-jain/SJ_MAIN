R=4
for i in range(R):
    for j in range(0,R-i):
        print("*",end=" ")              # * * * * * * * *   
    for k in range(i):                  # * * *     * * * 
        print(" ",end=" ")              # * *         * *     
        print(" ",end=" ")              # *             *    
    for l in range(R-i):                             
        print("*",end=" ")                         
    print()

# -------------------------------------------------------------

num_rows = int(input())
for i in range(num_rows):
    num_stars = num_rows - i  # Number of stars on each side
    num_spaces = 2 * i        # Number of underscores in the middle
    stars = '*' * num_stars
    spaces = ' ' * num_spaces
    pattern = stars + spaces + stars
    
    print(pattern)