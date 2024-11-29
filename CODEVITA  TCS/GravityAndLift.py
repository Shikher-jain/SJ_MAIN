def main():
#2 space separated

    n, m = map(int, input().strip().split())
    grid = []
    for _ in range(n):
        row = list(map(int, input().strip().split()))
        grid.append(row)
    

    # print("Grid Dimensions:", n, "x", m)
    # print("Grid:")
    # for row in grid:
    #     print(row)

    curr_row, curr_col = map(int, input().strip().split())
    
    dest_row, dest_col = map(int, input().strip().split())

if __name__ == "__main__":
    main()
