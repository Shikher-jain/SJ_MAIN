
arr.sort()
for i in range(n-1):
    ans=(arr[0]+arr[1])
    arr.append(arr.pop(0)+arr.pop(0))
    arr.sort()
    # print(arr)
print(ans)
