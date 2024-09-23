T = int(input())  
for _ in range(T):
    n=int(input())
    array = list(map(int, input().split()))
    odd = [str(i) for i in array if i % 2 != 0]
    even = [str(i) for i in array if i % 2 == 0]
    if not odd or not even:
        print()
    if odd:
        print(" ".join(odd)+" ")
    
    if even:
        print(" ".join(even)+" ")
