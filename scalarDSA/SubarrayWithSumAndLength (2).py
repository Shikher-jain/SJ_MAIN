def subArraySum(arr,l, sum):
    n=len(arr)
    if l==0 and l>n:
        return 0
    else:
        for i in range(n):
            if i+l>n:
            # currentSum = arr[i]
            # if(currentSum == sum):
            #     print("Sum found at indexes",i)
                return 0
            else:
                # Try all subarrays starting with 'i'
                # for j in range(i+1,n):
                currentSum=0
                for j in range(i,i+l):
                    currentSum += arr[j]
                    if(currentSum == sum):
                        # print("Sum found between indexes",i,"and",j)
                        return 1
        return 0
	# print("No Subarray Found")

# Driver Code
if __name__ == "__main__":
	# arr = [15,2,4,8,9,5,10,23]  
    arr = [1,2,3,4,5,6]
    arr = [6]
    n = len(arr)
    l=1
    sum = 6
    print(subArraySum(arr, l, sum))