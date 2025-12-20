#include <stdio.h>
#include <stdbool.h>

int main()
{
    int size =10;
    float suspect [size];
    float criminal [size];

    printf("Enter the 10 chromosomes of the suspect separated by spaces: \n");
    for(int i=0; i<size; i++)
    {
        scanf("%f",&suspect[i]);
    }

    printf("Enter the 10 chromosomes of the criminal separated by spaces: \n");
    for(int i=0; i<size; i++)
    {
        scanf("%f",&criminal[i]);
    }

    bool match = true;

    for(int i=0; i<size; i++)
    {
        if(suspect[i]!=criminal[i])
        {
            match = false;
        }
    }
    if(match==true)
    {
        printf("The two profile matches!!!\n");
    }
    else
    {
        printf("The two profile don't match! \n");
    }

    return 0;
}