class Solution:
    def rangeSum(self, A, B):
        # Step 1: Compute prefix sum array
        prefix_sum = [0] * (len(A) + 1)
        for i in range(1, len(A) ):
            prefix_sum[i] = prefix_sum[i - 1] + A[i]
        # Step 2: Compute sums for each query
        results = []
        for query in B:
            L, R = query
            # Check if L is greater than 0
            if L > 0:
                results.append(prefix_sum[R] - prefix_sum[L - 1])
            else:
                results.append(prefix_sum[R])
        return results
# Example usage:
obj = Solution()
# A = [1, 2, 3, 4, 5]
# B = [[1, 3], [0, 4], [2, 4]]
A=[]
B=[]
# Queries
n=int(input("Enter how any no. you want to enter in array A: "))
for i in range(n):
    A.append(int(input(f"Enter element on {i} index:\n")))
m=int(input("Enter How many Queries B you want to enter <[L,R]>\n"))
for j in range(m):
    Q=[]
    L=(int(input(("Enter L: "))))
    R=(int(input(("Enter R: "))))
    if(L<=R and L>=0 and R>=0 and L<= len(A) and R<=len(A) ):
        Q.append(L)
        Q.append(R)
        print(Q)
        B.append(Q)
        print(f"You entered {A}")
        print(B)
        print(obj.rangeSum(A, B))
    else:
        print("INVALID RANGE\nTRY AGAIN")
        break