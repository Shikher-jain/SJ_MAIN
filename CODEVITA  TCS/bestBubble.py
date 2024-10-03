def count(arr, target):
    n = len(arr)
    visited = [False] * n
    swaps = 0
    map = {val: i for i, val in enumerate(arr)}

    for i in range(n):
        if visited[i] or target[i] == arr[i]:
            continue 
        Csize = 0
        x = i
        while not visited[x]:
            visited[x] = True
            x = map[target[x]]
            Csize += 1
        if Csize > 0:
            swaps += (Csize - 1)

    return swaps

def Mswap(arr):
    sorted_asc = sorted(arr)
    sorted_desc = sorted(arr, reverse=True)
    ascending = count(arr, sorted_asc)
    descending = count(arr, sorted_desc)

    return min( ascending, descending)
# arr = [4,5,3,2,1]
arr=list(map(int,input().split()))
print(Mswap(arr))