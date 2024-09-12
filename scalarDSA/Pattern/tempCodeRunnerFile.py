def print_pattern(n):
    for i in range(n):
        for j in range(n):
            num = n - max(abs(i - (n-1)), abs(j - (n-1)))
            if num < 1:
                print("0", end=" ")
            else:
                print(num, end=" ")
        print()

n = 5
print_pattern(n)
