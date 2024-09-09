def fact(num):
    terms=0
    # for i in range(1,num+1):
    for i in range(1,int(num**0.5)+1):
        if (num % i==0):
            if(i*i != num):
                terms+=2
            else:
                terms+=1

    return terms
    # if (terms==1):
        # print(f"There is {terms} terms of Factor {num}")
    # else:
    #     print(f"There are {terms} terms of Factor {num}")
            
# fact(int(input("Enter the no. which you want the factors:")))
res=fact(417)
print(res)
res=fact(2)
print(res)
res=fact(16)
print(res)