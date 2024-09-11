R=int(input("ROWS: "))
# print(1,end="")
for i in range(1,1+R):                 # 1
    k=1                                # 1_ 
    for j in range(0,i,2):             # 1_3 
        if k==i:                       # 1_3_
            print(k,end="")            # 1_3_5
        else:                          
            print(k,end=" ")
        k+=2                           
    print()
