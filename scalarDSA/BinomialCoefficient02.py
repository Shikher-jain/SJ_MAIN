def binomial_coefficient(n, k):
    if k > n - k:  # take advantage of symmetry
        k = n - k
    result = 1
    for i in range(k):
        result *= (n - i)
        result //= (i + 1)
    return result

# Example usage:
n = 10
k = 2
result = binomial_coefficient(n, k)
print(f"Binomial Coefficient C({n}, {k}) = {result}")


# (k/n)=  n! / (k!(n−k)!)