#include <stdio.h>  
#include <stdlib.h>  
#define size 10
int deque[size],f = -1,r = -1; 

//  insert_front function will insert the value from the front    
void insert_front(int n) //#1   
{   
    int x;
    if((f==0 && r==n-1) || (f==r+1))     
    printf("Overflow"); 
    else if(f==0)
        printf("Queue isn't able to insert more value from front\n");
    else if((f==-1) && (r==-1)){    
        f=r=0;    
        printf("Enter the digit you want to insert ");
        scanf("%d",&x);
        deque[f]=x;    
    }
    else{
        printf("Enter the digit you want to insert ");
        scanf("%d",&x);
        f=f-1;    
        deque[f]=x;    
    }    
}    
   
// insert_rear function will insert the value from the rear    
void insert_rear(int n) //#2   
{    
    int x;
    if((f==0 && r==n-1) || (f==r+1))    
        printf("Overflow");    
    else if (r==n-1)
        printf("Queue isn't able to insert more value from rear\n");
    else if((f==-1) && (r==-1)){    
        f=r=0;   
        printf("Enter the digit you want to insert ");
        scanf("%d",&x); 
        deque[r]=x;    
    }    
        else{    
        printf("Enter the digit you want to insert ");
        scanf("%d",&x);
        r++;    
        deque[r]=x;    
    }     
}    

// delete_front() function deletes the element from the front    
void delete_front()  //#3  
{    
    if((f==-1) && (r==-1))  
        printf("Deque is empty");  
    else if(f==r){    
        printf("\nThe deleted element is %d", deque[f]);    
        f=-1;    
        r=-1;         
    }    
     else{    
          printf("\nThe deleted element is %d", deque[f]);    
          f=f+1;    
     }    
}    
    
// delete_rear() function deletes the element from the rear    
void delete_rear()  //#4  
{    
    if((f==-1) && (r==-1))
        printf("Deque is empty");     
    else if(f==r){    
        printf("\nThe deleted element is %d", deque[r]);    
        f=-1;    
        r=-1;    
    }
     else{    
          printf("\nThe deleted element is %d", deque[r]);    
          r=r-1;    
     }    
}    

// display function prints all the value of deque.    
void display()  //#5  
{    
    int i=f;    
    printf("\nElements in a deque are: ");
    while(i!=r+1)
    {    
        printf("%d ",deque[i]);    
        i=i+1;   
    }      
}    

void main(){  
    int ch=0,n;
    printf("Enter no. of elements in Queue:");
    scanf("%d",&n);
    if(size<n)
    printf("Plz I/P the elements less then %d",size);
    else{
    for(;;){//infinite loop
    printf("\n f=%d r=%d\n",f,r);
    printf("\n1 for insert front\n2 for insert rear\n3 for delete front\n4 for delete rear\n5 for Display\n6 for Existing\n");
    scanf("%d",&ch);
    switch(ch){
    case 1:insert_front(n);break;
    case 2:insert_rear(n);break; 
    case 3:delete_front();break;
    case 4:delete_rear();break;
    case 5:display();break;
    case 6:printf("Existing...");exit(0);
    default:printf("Invalid input");
    }//switch case
    }//while
    }//else
}    //main
    
    // insert_front(20);    
    // insert_front(10);    
    // insert_rear(30);    
    // insert_rear(50);    
    // insert_rear(80);    
    // display();  // Calling the display function to retrieve the values of deque    
    
    // delete_front();    
    // delete_rear();    
    // display(); // calling display function to retrieve values after deletion
