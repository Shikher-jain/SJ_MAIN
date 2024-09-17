arr=list(map(int,input().split()))
# arr=[5, 1, -5, 2, -8, -4]
arr1=[]
# print(arr) 
n=len(arr)
for i in range(n):
    if arr[i]<=0:
        arr1.append(arr[i])

# print(arr) 
# print(arr) 
print(" ".join(map(str,arr1)),end=" ") 