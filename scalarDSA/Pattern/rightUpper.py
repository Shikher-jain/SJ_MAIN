R=int(input("Enter how many Rows you wants to print: "))        #|* * * * * * *    R=7
for i in range(R):                                              #|  * * * * * *
    for j in range(i):                                          #|    * * * * *
        print(" ",end=" ")                                      #|      * * * *
    for k in range(R-i):                                        #|        * * *
        print("*",end=" ")                                      #|          * *        
    print()                                                     #|            *

