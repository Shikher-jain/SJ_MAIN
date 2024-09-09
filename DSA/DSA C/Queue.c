
//Queue implementation in C

#include <stdio.h>
#include<stdlib.h>
#define Arr 100
int items[Arr], front = -1, rear = -1,n;
void enQueue(int n) {
  if (rear == n - 1)
    printf("\nQueue is Full!!");
  else {
    if (front == -1)
      front = 0;
    rear++;
    int value;
    printf("Enter No.");
    scanf("%d",&value);
    items[rear] = value;
    printf("\nInserted -> %d", value);
  }
}
void deQueue() {
  if (front == -1)
    printf("\nQueue is Empty!!");
  else {
    printf("\nDeleted : %d", items[front]);
    front++;
    if (front > rear)
      front = rear = -1;
  }
}
void display() {
  if (rear == -1)
    printf("\nQueue is Empty!!!");
  else {
    int i;
    printf("\nQueue elements are:\n");
    for (i = front; i <= rear; i++)
      printf("%d  ", items[i]);
  }
  printf("\n");
}


int main() {
    int ch=0;
    printf("Enter no. of elements in Queue:");
    scanf("%d",&n);
    if(Arr<n)
    printf("Plz I/P b/w 0 to 100");
    else{
   while(ch!=4){
    printf("\n1 for Enqueue\n2 for Dnqueue\n3 for Display\n4 for Existing\n");
    scanf("%d",&ch);
    
    switch(ch){
    case 1:enQueue(n);break;
    case 2:deQueue();break;
    case 3:display();break;
    case 4:printf("Existing...");exit(0);
    default:printf("Invalid input");
    }}
 return 0;
}
}