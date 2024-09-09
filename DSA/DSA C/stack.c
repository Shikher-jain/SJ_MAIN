//STACK 
#include<stdio.h>
#include<stdlib.h>
typedef struct stack{
    int size;
    int top;
    int *arr;
    }S;
//CHECK FOR EMPTY
int empty(S*ptr){
    if(ptr->top==-1)
        return 1;
    return 0;
}
//CHECK FOR FULL
int full(S*ptr){
    if(ptr->top==ptr->size-1)
        return 1;
    return 0;
}
//FOR PUSH
void push(S*ptr,int value){
    if(full(ptr)){
        printf("STACK OVERFLOW!\n");
        printf("Can't be push %d to the stack\n",value);
    }
    else
{
    ptr->top++;
    ptr->arr[ptr->top]=value;
}
}
//FOR POP
int pop(S*ptr){
    if(empty(ptr)){
        printf("STACT UNDERFLOW\n");
        printf("Can't pop from the stack\n");
    return-1;
    }
    else{
        int val=ptr->arr[ptr->top];
        ptr->top--;
        return val;
    }
    }
// //FOR PEEK
// int peek(S*ptr,int j){
//     int index=ptr->top-j+1;
//     if(index<0){
//         printf("Invalid position\n");
//     return -1;    
//     }
//     else{
//         return ptr->arr[index];
//     }
// }
//TOP ELEMENT
int top(S*ptr){
    return ptr->arr[ptr->top];
}
//BOTTOM OR FIRST ELEMENT
int bottom(S*ptr){
    return ptr->arr[0];
}
//MAIN FUNCTION
void main()
{
    int item,insert,delete;
    S*ptr=(S*)malloc(sizeof(S));
    // ptr->size=10;
    printf("Enter the size:\n");
    scanf("%d",&ptr->size);
    printf("Enter the no. of Element you want to insert in STACK\n");
    scanf("%d",&insert);
    ptr->top=-1;
    ptr->arr=(int*)malloc(ptr->size*sizeof(int));
    printf("Stack has been created successfully\n");
    printf("Before pushing,full:%d\n",full(ptr));
    printf("Before pushing,empty:%d\n \n",empty(ptr));
    // push(ptr,0);
    // push(ptr,1);
    // push(ptr,2);
    // push(ptr,3);
    // push(ptr,4);
    // push(ptr,5);
    // push(ptr,6); 
    // push(ptr,7);
    // push(ptr,8);
    // push(ptr,9);
    // push(ptr,10);//OVERFLOW not count while poping
    
    for (int i = 1;i <= insert; i++)
    {
        printf("Enter %d Element to push in STACK\n",i);
        scanf("%d",&item);
        push(ptr,item);
    }
    
    printf("\nAfter pushing,full:%d\n",full(ptr));
    printf("After pushing,empty:%d\n\n",empty(ptr));
   
    printf("How many elements you should POP from STACK\n");
    scanf("%d",&delete);
    for (int i = 1;i <= delete; i++){
        int z = pop(ptr);
        if(z==-1)
        break;
        else
        printf("%d popped from the stack\n",z);
    }
   
    // printf("%d popped from the stack\n",pop(ptr));
    // printf("%d popped from the stack\n",pop(ptr));
    // printf("%d popped from the stack\n",pop(ptr));
    // printf("%d popped from the stack\n",pop(ptr));
    // printf("%d popped from the stack\n",pop(ptr));
    // printf("%d popped from the stack\n",pop(ptr));
    // printf("%d popped from the stack\n",pop(ptr));
    // printf("%d popped from the stack\n",pop(ptr));
    // printf("%d popped from the stack\n",pop(ptr));
    // printf("%d popped from the stack\n",pop(ptr));//UNDERFLOW
    // printf("%d popped from the stack\n",pop(ptr)); 

    // for (int j = 1; j < ptr->top+1; j++) {
    //     printf("The value of %d if %d\n",j,peek(ptr,j));
    // }
    printf("\nThe top most value of this stack %d\n",top(ptr));
    printf("The bottom most value of this stack %d\n",bottom(ptr));
}