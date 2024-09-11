
R=int(input("Enter how many Rows you wants to print: "))
for i in range(1,1+R):          # 1 
    k=1                         # 1 2 
    for j in range(i):          # 1 2 3 
        print(k,end=" ")        # 1 2 3 4 
        k+=1                    # 1 2 3 4 5 
    print()

