#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct stack{
    int top;
    int size;
    char * arr;
}S; 
int empty(S* ptr){
    if(ptr->top==-1){
        return 1;
    }
    else{
        return 0;
    }
}
int full(S* ptr){
    if(ptr->top==ptr->size - 1){
        return 1;
    }
    else{
        return 0;
    }
}
void push(S*ptr,char value){
    if(full(ptr)){
        printf("STACK OVERFLOW");
    }
    else{
        ptr->top++;
        ptr->arr[ptr->top]=value;
    }
}
char pop(S* ptr){
    if (empty(ptr))
    {
        printf("STACK UNDERFLOW");
        return -1;
    }
    else
    {
        char val=ptr->arr[ptr->top];
        ptr->top--;
        return val;
    }
}
int precedence(char ch){
    if (ch=='-'||ch=='+')
        return 2;//low precedence
    else if (ch=='/'||ch=='*')
        return 3;//high precedence
    else    
    return 0;
}
int top(S* ptr){
    return ptr->arr[ptr->top];
}
int operator(char ch){
    if (ch!='+'|| ch!='*'|| ch!='/'|| ch!='-')
    return 1;
    else
    return 0;
    }
char* inflixToprefix(char*inflix){ 
S*ptr=(S*)malloc(sizeof(S));
ptr->size=30;
ptr->top=-1;
ptr->arr=(char*)malloc(sizeof(char) * ptr->size);
char* prefix=(char*)malloc((strlen(inflix)+1)*sizeof(char));
int i=0;
int j=0;
while (inflix[i]!='\0'){
    if(!operator(inflix[i])){
        prefix[j]=inflix[i];
        j++;
        i++;
    }
    else{
        if (precedence(inflix[i])>precedence(top(ptr))){
            push(ptr,inflix[i]);
            i++;
        }
        else{
            prefix[j]=pop(ptr);
            j++;
            }
        }
    }
    while (!empty(ptr)){
            prefix[j]=pop(ptr);
            j++;
        }
        prefix[j]='\0';
        return prefix;
    }
int main(){
    char * inflix ="r-t+y/t*y-y";
    // r-t+(y/t)*y-y --- INFLIX
    // r-t+(/yt)*y-y
    // r-t+(*/yty)-y
    // (-rt)+(*/yty)-y
    // +(-rt*/yty)-y
    // -+-rt*/ytyy --- PREFIX
printf("preFIX IS %s", inflixToprefix(inflix));
    return 0;
}