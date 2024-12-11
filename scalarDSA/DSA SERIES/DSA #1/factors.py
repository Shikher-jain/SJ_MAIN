import math

A=10

cnt = 0
Factor=[]
for i in range(1, int(math.sqrt(A)) + 1):
    if A % i == 0:  # If A is divisible by i
        cnt += 1  # Count divisor i

        if i != A // i:  # Avoid counting the same divisor twice
            cnt += 1  # Count divisor A // i
print(cnt)
print(Factor)





cnt = 0

Factor=[]
for i in range(1, A + 1):
    if A % i == 0:  # If A is divisible by i
        cnt += 1  # Count divisor i
        Factor.append(i)
        
print(cnt)
print(Factor)