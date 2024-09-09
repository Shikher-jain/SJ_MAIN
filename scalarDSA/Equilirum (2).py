# A = [-7, 1, 5, 2, -4, 3, 0]

# def Sum(A):
#     p=[0]*len(A)
#     p[0]=A[0]
#     for i in range(len(A)):
#       p[i]=p[i-1]+A[i]
#     return p
# S=Sum(A)
# print("Array",A)
# print("PreSum",S)

# # =======

# def solve1(A):
#     sum_arr = sum(A)  #pre-sum

#     left_sum = 0
#     right_sum = sum_arr - A[0]
#     if left_sum == right_sum:
#         return 0

#     for i in range(1,len(A)):
#         left_sum += A[i-1]
#         right_sum -= A[i]

#         if left_sum == right_sum:
#             return i
#         return -1
    
# # s=solve1(A)
# # print(s)
# # s=solve1(S)
# # print(s)

# def solve2(A):
#     # n = len(A)
#     # # psum = [0] * n
#     # psum = []
#     # # print("presum\n",psum)
#     # psum = A
#     # for i in range(1, n):
#     #     psum[i] = psum[i-1] + A[i]
#     psum=Sum(A)
#     for i in range(len(A)):
#         left_sum = 0
#         if i > 0:
#             left_sum = psum[i-1]
#         right_sum = psum[-1] - psum[i]
#         print(left_sum,right_sum)
#         if left_sum == right_sum:
#             return i
#     return -1


# # s=solve2(A)
# # print(s)

# def solve3(A):
#     pre=Sum(A)
#     l=0
#     for i in range(len(A)):
        
#     #    print(Sum(A[0:i+1]))
#        if Sum( A[0:i] ) == Sum( A[i+1:len(A)] ):
#            return i
#     #    return -1

# S=solve3(A)
# print(S)

# # function to find the equilibrium index
def equilibrium(arr):
	leftsum = 0
	rightsum = 0
	n = len(arr)

	# Check for indexes one by one
	# until an equilibrium index is found
	for i in range(n):
		leftsum = 0
		rightsum = 0

		# get left sum
		for j in range(i):
			leftsum += arr[j]

		# get right sum
		for j in range(i + 1, n):
			rightsum += arr[j]

		# if leftsum and rightsum are same,
		# then we are done
		if leftsum == rightsum:
			return i

	# return -1 if no equilibrium index is found
	return -1


# Driver code
if __name__ == "__main__":
	arr = [-7, 1, 5, 2, -4, 3, 0]

	# Function call
	print(equilibrium(arr))

# This code is contributed by Abhishek Sharama

    