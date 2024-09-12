
n=5

for i in range(1, n + 1):
    # Print leading spaces
    print("0 " * (n - i), end="")
    
    # Print increasing part of the pattern
    start = i
    for j in range(i):
        print(start + j, end=" ")
    
    # Print decreasing part of the pattern
    for j in range(i - 1):
        print(start + i - 2 - j, end=" ")
    
    print("0 " * (n - i), end="")
    # Move to the next line
    print()



# 0 0 0 0 1 0 0 0 0         . . . . 1 0 0 0 0       4 > 0 - 1
# 0 0 0 2 3 2 0 0 0         . . . 2 3 2 0 0 0       3 > 0 - 2 3 
# 0 0 3 4 5 4 3 0 0         . . 3 4 5 4 3 0 0       2 > 0 - 3 4 5
# 0 4 5 6 7 6 5 4 0         . 4 5 6 7 6 5 4 0       1 > 0 - 4 5 6
# 5 6 7 8 9 8 7 6 5         5 6 7 8 9 8 7 6 5       0 > 0 - 5 6 7 8


