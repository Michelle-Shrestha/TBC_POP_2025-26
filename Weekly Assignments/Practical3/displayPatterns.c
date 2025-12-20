#include <stdio.h>

//PATTERNS
int main ()
{
    int size = 6;
    //using temp as copy variable of size to not affect the actual size variable
    int temp = size;
    int temp2 = size;

    printf("Patter A: \n");
    for(int i=1;i<=size;i++)
    {
        for (int j =1;j<=i;j++)
        {
            printf("%d ",j);
        }
        
        printf("\n");
    }
    printf("\n\n");

    printf("Pattern B: \n");
    for(int i=1;i<=size;i++)
    {
        
        for(int j =1; j<=temp;j++)
        {
            printf("%d ",j);
        }
        temp-=1;
        
        printf("\n");
    }
    printf("\n\n");

    printf("Pattern C: \n");
    for(int i=1;i<=size;i++)
    {
        for(int space =i;space<size;space++)
        {
            printf("  ");
        }
        //reversing the pattern
        for(int j=i; j>=1;j--)
        {
            printf("%d ",j);
        }
        //temp2-=1;
        printf("\n");
    }
    printf("\n\n");

    printf("Pattern D: \n");
    for(int i=1;i<=size;i++)
    {
        for(int space=1;space<i;space++)
        {
            printf("  ");
        }
        for(int j = 1;j<=temp2;j++)
        {
            printf("%d ",j);
        }
        temp2-=1;
        printf("\n");
    }
    return 0;
}