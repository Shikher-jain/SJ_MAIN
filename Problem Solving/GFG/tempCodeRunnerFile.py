# print(a)
'''
             |
       |     |
       |     |
   |   |     |
   |   | |   |
   |   | |   |
   | | | | | |
   | | | | | |
   | | | | | |       ~ X ~ X X ~
a=[7,3,8,5,3,9]  --> 7 3 8 5 3 9   --> 3
'''
def solve(a):
    # ans=1
    ans=1
    n=len(a)
    m=len(a)
    high=a[0]
    if n==1:
        return ans
    i=1
    while i<m:
        if a[i] > high:    
            ans+=1
            high=a[i]
    return ans


# arr=list(map(int,input("LIST").split()))
arr=[7,3,8,5,3,9]        
# arr=[2,3,4,5]
arr=[7, 7, 8, 3, 2, 8, 9, 7]
print(solve(arr))