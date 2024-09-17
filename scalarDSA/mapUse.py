def insert_element_at_position(arr, x, y):
    index =  x - 1
    arr.insert(index, y)
    return arr

def main():
    N = int(input())
    arr = list(map(int, input().split()))
    X = int(input())
    Y = int(input())
    updated_array = insert_element_at_position(arr, X, Y)
    print(' '.join(map(str, updated_array)),end=" ")

if __name__ == "__main__":
    main()
