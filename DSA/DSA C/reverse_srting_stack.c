// WAP ic c to reverse the string by using stack implementation
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Stack {
    int top;
    unsigned capacity; // only for '+' integers //Also refer as size
    char* array;
};
//stack capacity
struct Stack* createStk(unsigned capacity)
{
    struct Stack* stack=(struct Stack*)malloc(sizeof(struct Stack));
    stack->capacity = capacity;
    stack->top = -1;
    stack->array = (char*)malloc(stack->capacity * sizeof(char));//stact capacity
    //jitni capacity unta space allocated
    return stack;
}
// Stack is full when top is equal to the last index
int isFull(struct Stack* stack)
{
    return stack->top == stack->capacity - 1;
}
// Stack is empty when top = -1
int isEmpty(struct Stack* stack)
{
    return stack->top == -1;
}
// Function to push a element.
// It increases top by 1
void push(struct Stack* stack, char item)
{
    if (isFull(stack))
        return;
    stack->array[++stack->top] = item; 
    /*stack->top++;                      // also used this
    stack->array[stack->top]=item;*/
}
// Function to pop a element
// It decreases top by 1
char pop(struct Stack* stack)
{
    if (isEmpty(stack))
        // printf("STACT UNDERFLOW\n");
        return INT_MIN;//----------> isme koi bhi specify limit ke bahr value store nhi hogi
        // ------------------------> aur #include<limits.h> ka use hota h
        //-------------------------> INT_MIN ka mtlb minimum value for int.
        // printf("Can't pop from the stack\n");
    // return-1;
    return stack->array[stack->top--];
}
//function to reverse a string
void rev(char str[])
{
    //stack of capacity{size} which is equal to length of str.
    int n = strlen(str);
    int i;
    struct Stack* stack = createStk(n);
    // Push all elements to stack
    for (i = 0; i < n; i++)
        push(stack, str[i]);
    // Pop all elements of str.
    // put it back to str.
    for (i = 0; i < n; i++)
        str[i] = pop(stack);
}

int main()
{
    char str[] = "Teri dosti ne bahut kuch sikha diya, udas chehre ko hasna sikha diya me karj dar hu us khuda ka jisane mujhe tere jaise dost se mila diya... by shikher";
    // printf("Enter string:\n");
    // gets(str);
    char str1[]="rehkihs yb ...ayid alim es tsod esiaj eret ehjum enasij ak aduhk su uh rad jrak em ayid ahkis ansah ok erhehc sadu ,ayid ahkis hcuk tuhab en itsod ireT";
    rev(str);
    rev(str1);
    printf("Reversed string is %s\n\n\n", str);
    printf("Reversed string is %s", str1);
    return 0;
}