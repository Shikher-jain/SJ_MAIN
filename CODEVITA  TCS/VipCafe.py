import sys

def main():
    n = int(input())
    priorities = list(map(int, input().split()))
    k = int(input()) - 1  # Adjust to 0-based index
    
    served = 0
    while True:
        max_priority = max(priorities)
        max_index = priorities.index(max_priority)
        served += 1
        
        if max_index == k:
            break
        
        for i in range(max_index):
            priorities[i] += 1
        
        priorities = priorities[:max_index] + priorities[max_index+1:]
        if k > max_index:
            k -= 1
    
    print(served)

if __name__ == "__main__":
    main()

