#     #Sum of element From L position to R position
def preSum(A,L,R):
    for i in B:
            L=i[0]
            R=i[1]
    # A=[-6,3,2,4,5-2,1,9]
    p=[]
    p=A
    sum=0
    for i in range(L,R+1):
        # A[i]=A[i-1]+A[i]
            sum+=p[i]
            # p[i]=p[i-1]+A[i]
        # ans =A[i]-A[L-1]
            return sum
    # print(p)
#         # 0 1 2 3 x4 5 6 7 
#     # A: -6,3,2,4,5-2,1,9
#     # p: -6,3,2,4,5-2,1,9

#     # Updated p wil be:

#     # p: -6,-3,-1,3,6,7,16

#     #Sub array add
#     # a=[8,6,5]
#     # [8], [6], [5], [8,6], [6,5], [8,6,5]

# def sumOfSubarray2(A):
#     ans=0 
#     sum=0
#     for i in range(len(A)):
#         # sum=A[i]*(i+1)*(len(A)-i)
#         ans+=A[i]*(i+1)*(len(A)-i)
#         # ans+=sum
#     return ans

# def sumOfSubarray1(A):
#     ans=0 
#     for i in range(len(A)):
#         sum=0
#         for j in range(i,len(A)):
#             sum+=A[j]
#             ans+=sum
#     return ans

# A=[-6,3,2,4,5-2,1,9]


# print(sumOfSubarray1(A))
# print(sumOfSubarray2(A)) 

class Solutiion:
    def sum(self,A,B):
        # L=A[0]
        # R=A[len(A)-1]
        print(A);print(B)
        for i in B:
            L=i[0]
            R=i[1]
            # print(L,R)
            Sum=preSum(A,L,R)
            print(Sum)
A=[-6,3,2,4,5-2,1,9]   #ARRAY 
B=[[0,0],[0,3],[2,6]]  #SUBARRAY [L,R] e.g.  A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R]
sol=Solutiion()
sol.sum(A,B)