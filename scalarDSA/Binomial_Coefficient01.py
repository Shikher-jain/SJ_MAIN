import math

def binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


n = 10
k = 2
result = binomial_coefficient(n, k)
print(f"Binomial Coefficient C({n}, {k}) = {result}")


# (k/n)=  n! / (k!(n−k)!)

