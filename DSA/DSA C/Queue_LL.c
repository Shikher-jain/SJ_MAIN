#include <stdio.h>
#include <stdlib.h>
 
typedef struct Node{
    int data;
    struct Node *next;
}S;
 
S  *f = NULL;
S  *r = NULL;
 
void display(S  *ptr)
{
    if(r==NULL)
    printf("Empty");
    else{
    printf("Printing the elements of this linked list\n");
    while (ptr != NULL)
    {
        printf("Element: %d\n", ptr->data);
        ptr = ptr->next;
    }
}}
 
void enqueue()
{
    int val;
    struct Node *n = (struct Node *) malloc(sizeof(struct Node));
    if(n==NULL){
        printf("Queue is Full");
    }
    else{
        
        printf("Enter No. to insert an element in queue");
        scanf("%d",&val);
        n->data = val;
        n->next = NULL;
        if(f==NULL){
            f=r=n;
        }
        else{
            r->next = n;
            r=n;
        }
    }
    printf("%d is inserted",val);
}
 
void dequeue()
{
    int val = -1;
    struct Node *ptr = f;
    if(f==NULL){
        printf("Queue is Empty\n");
        printf("Dequeuing element %d\n", val);
    }
    else{
        f = f->next;
        val = ptr->data;
        free(ptr);
        printf("Dequeuing element %d\n", val);
    }
}
int main() {
    int ch=0;
    while(ch!=4){
    printf("\n1 for Enqueue\n2 for Dnqueue\n3 for Display\n4 for Existing\n");
    scanf("%d",&ch);
    switch(ch){
    case 1:enqueue();break;
    case 2:dequeue();break;
    case 3:display(f);break;
    case 4:printf("Existing...");exit(0);
    default:printf("Invalid input");
    }}
 return 0;
}
