def bubble(n,arr,order=True):
      
  swap=0
  for i in range(n):
    for j in range(n-i-1):
      if (not order and arr[j]<arr[j+1]) or (order and arr[j]>arr[j+1]):#D , A
        arr[j+1],arr[j]=arr[j],arr[j+1]
        swap+=1
  return swap 

def Mswap(n,arr):
  ascendingOrder=bubble(n,arr[:],order=True)
  descendingOrder=bubble(n,arr[:],order=False)
  return min(ascendingOrder,descendingOrder)
  
n=int(input())
arr=list(map(int,input().split()))
print(Mswap(n,arr))
