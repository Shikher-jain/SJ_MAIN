def solve(n):
   iteration=0
   for i in range(n):
        for j in range(i // 2):
            # O(1) operation
            iteration+=1
        return iteration
res=solve(10)
print(res)