#include<stdio.h>
int main()
{
    int a,b,c,d,e,f,g;
    printf("Enter the marks of subject 1 :");
    scanf("%d",&a);
    printf("Enter the marks of subject 2 :");
    scanf("%d",&b); 
    printf("Enter the marks of subject 3 :");
    scanf("%d",&c); 
    printf("Enter the marks of subject 4 :");
    scanf("%d",&d); 
    printf("Enter the marks of subject 5 :");
    scanf("%d",&e); 
    f=a+b+c+d+e;
    printf("The sum of all subject is : %d\n-------------------------------\n",f);
    float per=f/5;
    printf("Percentage obtained: %f",per);
return 0;
}