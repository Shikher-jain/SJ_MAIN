T = int(input())
for _ in range(T):
    A = int(input())
    array = list(map(int, input().split()))
    B = int(input())    
    if B in array:
        print(1)
    else:
        print(0)