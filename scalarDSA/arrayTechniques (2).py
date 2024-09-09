#   0 1 2 3 4 5 6 7
A=[-6,3,2,4,5-2,1,9]   #ARRAY 
B=[[0,0],[0,3],[2,6]]  #SUBARRAY [L,R] e.g.  A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R]
p=[]
p=A
for i in range(len(B)): #3
    L=B[i][0]
    R=B[i][1]
    if L<=R:
        sum=0
        for j in range(L,R+1):
            sum+=p[j]
    print(sum)