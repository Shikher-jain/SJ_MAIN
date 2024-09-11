
R=int(input("Enter how many Rows you wants to print: "))  
x=input("Enter symbol : ")    
if len(x)==1:
    for i in range(1,R+1):                                        
        for j in range(R-i):                   #|   R=6      
            print(" ",end=" ")                 #|          * 
        for k in range(i):                     #|        * * *
            print(x,end=" ")                   #|      * * * * *    
        for l in range(i-1):                   #|    * * * * * * *
            print(x,end=" ")                   #|  * * * * * * * * *
        print()                                #|* * * * * * * * * * *
else:
    raise Exception("INVALID !!")

