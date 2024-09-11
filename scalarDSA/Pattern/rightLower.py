
R=int(input("Enter how many Rows you wants to print: "))        #|            *  R=7
for i in range(1,R+1):                                          #|          * *
    for j in range(R-i):                                        #|        * * *
        print(" ",end=" ")                                      #|      * * * * 
    for k in range(i):                                          #|    * * * * *
        print("*",end=" ")                                      #|  * * * * * *
    print()                                                     #|* * * * * * *

