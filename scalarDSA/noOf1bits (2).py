def numOf1Bits(A):
    b = A
    res = 0
    while b > 0:
        if b & 1:
            res += 1
        b >>= 1
    return res

print(numOf1Bits(6))
# for i in range(9):
#     print(numOf1Bits(i))

# 8 4 2 1
# 0 1 1 0 -- 6
#   ^ ^