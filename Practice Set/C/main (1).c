/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
void main()
{
    int n,i,item,a[50],first=0,last=n-1,mid=(first+mid)/2;
    printf("\nEnter Sorted data only");
    printf("\nEnter the no. element ");
    scanf("%d",&n);
    printf("Enter the elements of array \n ");
    for(i=0;i<n;i++)    
    scanf("%d",&a[i]);
    for(i=0;i<n;i++)
    printf(" %d",a[i]);
    printf("\nEnter the element to be search ");
    scanf("%d",&item);
    while(first<=last)
    {
        if(item<mid)
        {
            last=mid-1;
            printf("%d %d",item,last);
        }
    else if(item==mid)
  {  printf("%d %d",item,mid);
   } else
    {
        first=mid+1;
        printf("%d %d",item,first);
    }
        
    }
    if(first>last)
    printf("\nUnsuccessful");
}
   /* for(i=0;i<n;i++)
    {
        if(item==a[i])
       { flag =1;
         break;
       }
    }
    if(flag==1)
        printf("\nSuccess item is on %dth position ",i+1);
       
        else
        printf("\nUnsuccessful Search");

}*/
