def generate_pattern(n):
    size = 2 * n - 1
    matrix = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(n):
        # Set values across each layer
        for j in range(i, size - i):
            matrix[i][j] = n - i
            matrix[j][i] = n - i
            matrix[size - i - 1][j] = n - i
            matrix[j][size - i - 1] = n - i

    # Print the matrix
    for row in matrix:
        print(" ".join(map(str, row)))

n = 5
generate_pattern(n)
