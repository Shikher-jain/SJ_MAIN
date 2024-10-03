def longest_contiguous_zeros(B, K):
    Z = B - K  # Total number of zeros
    if K == 0:  # All zeros
        return Z
    if K >= B:  # All ones
        return 0
    
    # Calculate how to distribute zeros
    base = Z // (K + 1)
    extra = Z % (K + 1)
    
    # If there are extra zeros,
    #  the maximum length of zeros will be base + 1

    if extra > 0:
        return base + 1
    else:
        return base


B = int(input())
K = int(input())
# B = 3   
# K = 1   
result = longest_contiguous_zeros(B, K)
print(result) 
