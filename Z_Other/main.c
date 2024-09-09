/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include<stdio.h>
#include<ctype.h>
int main() {
    char c;
    printf("Enter a character: ");
    scanf("%c", &c);

    if (isalpha(c))
    printf("%c is an alphabet.", c);
else
    printf("%c is not an alphabet.", c);
return 0;
    
}