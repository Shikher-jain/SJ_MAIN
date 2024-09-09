#include<stdio.h>

void main(){
    int A=16;
    int res = 0 ;
    for (int i = 1 ; i*i <= A ; i++){
        if(A%i == 0){
        if(i*i != A)
        res += 2 ;
        else res ++;
        }
    }
    // return res;
    printf("%d",res);
}
