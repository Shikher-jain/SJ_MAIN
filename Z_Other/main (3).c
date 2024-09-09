#include<stdio.h>
/*1. WAP that accepts the marks of 5 subjects and finds the sum and percentage marks obtained by the student.*/
void main() 
{
	float hindi, english, science,math,computer,sum ;
	float per;
	printf("Enter marks of Hindi=");
	scanf("%f",&hindi);
	printf("Enter marks of English=");
	scanf("%f",&english);
	printf("Enter marks of Science=");
	scanf("%f",&science);
	printf("Enter marks of Math=");
	scanf("%f",&math);
	printf("Enter marks of Computer=");
	scanf("%f",&computer);
	
	sum=hindi+english+science+math+computer;
	printf("Sum of marks=%f",sum);
	
	per=(float)sum/5;
	printf("Percentage of marks=%f",per);
	printf("\n Your Grade is ");
    if((per<=100)&&(per>=90))
    printf("A");
    if((per<90)&&(per>=80))
    printf("B");
    if((per<80)&&(per>=60))
    printf("C");
    if(per<60)
    printf(" D");
}
    
    
    
    



