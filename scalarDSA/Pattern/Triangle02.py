R=int(input("Enter how many Rows you wants to print: "))
for i in range(R):
    for j in range(R, i, -1):           #      * 
        print(" ", end="")              #     * *
    for k in range(i + 1):              #    * * *
        print("* ", end="")             #   * * * *
    print()                             #  * * * * *

