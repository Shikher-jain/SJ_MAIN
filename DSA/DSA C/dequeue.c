#include <stdio.h>
#include <stdlib.h>
#define size 5
int arr[size],R=-1,F=-1,temp=0,n,x;

void rear_insert(){
    if(temp==size)
        printf("Queue is full");
    else{
        if(F==-1)
            F=0;
        printf("Enter a number ");
        scanf("%d",&n);
        // R=(R+1)%size;//circular
        R=R+1;
        arr[R]=n;
        temp=temp+1;
    }
}
void rear_del(){
    if(R!=size-1||temp!=0){
        printf("Number Deleted From Rear End = %d",arr[R]);
        R=R-1;
        temp=temp-1;
    }
    else
        printf("Queue is empty");
}
void front_insert(){
    if(temp==size)
        printf("Queue is full");
    else{
        printf("Enter a number ");
        scanf("%d",&n);
        F=F-1;
        arr[F]=n;
        temp=temp+1;
    }
}
void front_del(){
    if(F==-1||F==size)
        printf("Queue is empty");
    else{
        printf("Number Deleted From Front End = %d",arr[F]);
        F=F+1;
        temp=temp-1;
        }
}
void display(){
        if(temp==0||R==-1)
        printf("Queue is empty");
    else{
        for(int i=F; i<=R; i++)
            printf("%d ",arr[i]);
        }
}
void main(){
    int ch,a;
    // for(;;)		// An infinite loop
    while(a!=0){
        printf("\nF=%d  R=%d\n1. Add Rear\n2. Delete Rear\n3. Add Front\n4. Delete Front\n5. Display\n6. Exit\n",F,R);
        printf("Enter Choice: ");
        scanf("%d",&ch);
        switch(ch){
            case 1:rear_insert();break;
            case 2:rear_del();break;
            case 3:front_insert();break;
            case 4:front_del();break;
            case 5:display();break;
            case 6:exit(0);break;
            default:printf("Wrong Choice");
        }
    }
}