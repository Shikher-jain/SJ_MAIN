#include <stdio.h>
// C recursive function to solve tower of hanoi puzzle
void Hanoi(int n,char from,char to,char aux){
    if (n == 1){
        printf("\n Move disk 1 from rod %c to rod %c", from,to);
        return;
    }
    Hanoi(n-1,from,aux,to);
    printf("\n Move disk %d from rod %c to rod %c", n, from,to);
    Hanoi(n-1,aux,to,from);
}
int main(){
    int n ;
    printf("Number of disks");
    scanf("%d",&n);
    Hanoi(n, 'A', 'C', 'B');  // A, B and C are names of rods
    return 0;
}

