n=5
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    
    # Print increasing part of the pattern
    start = i
    for j in range(i):
        print(start + j, end=" ")
    
    # Print decreasing part of the pattern
    for j in range(i - 1):
        print(start + i - 2 - j, end=" ")

    print()
