
R=int(input("Enter how many Rows you wants to print: "))
k=1
for i in range(1,1+R):          # 1 
    for j in range(i):          # 2 3
        print(k,end=" ")        # 4 5 6
        k+=1                    # 7 8 9 10
    print()                     # 11 12 13 14 15
