
R=int(input("Enter how many Rows you wants to print: "))        
for i in range(1,R+1):                          #|*                   * 
    for j in range(i):                          #|* *               * * 
        print("*",end=" ")                      #|* * *           * * *    R=6
    # for k in range(R-i):                      #|* * * *       * * * * 
    for k in range(2*(R-i)):                    #|* * * * *   * * * * * 
        print(" ",end=" ")                      #|* * * * * * * * * * * 
    # for k in range(R-i):                                    
        # print(" ",end=" ")                                    
    for l in range(i):                                         
        print("*",end=" ")                                      
    print()                                                  



# R=int(input("Enter how many Rows you wants to print: "))        
# for i in range(1,R+1):                          #|*                   * 
#     for j in range(i):                          #|* *               * * 
#         print("*",end="")                       #|* * *           * * *    R=6
#     # for k in range(R-i):                      #|* * * *       * * * * 
#     for k in range(2*(R-i)):                    #|* * * * *   * * * * * 
#         print(" ",end="")                       #|* * * * * * * * * * * 
#     # for k in range(R-i):                                    
#         # print(" ",end=" ")                                    
#     for l in range(i):                                         
#         print("*",end="")                                      
#     print()                                                  
