#include<stdio.h>
#include <stdbool.h>

int main(){
    int size = 10;
    bool match = true;
    //declaring suspect array
    float suspect[size]; 
    //declaring criminal array
    float criminal[size]; 
    //read 10 input values into suspect array from keyboard
    printf("Enter the 10 chromosomes of the suspect separated by spaces: \n");
    for (int i = 0; i < size; i++)
        {
            scanf(" %f", &suspect[i]);
        }
    //read 10 input values into criminal array from keyboard
    printf("Enter the 10 chromosomes of the criminal separated by spaces: \n");
    for (int i = 0; i < size; i++)
    {
        scanf(" %f", &criminal[i]);
    }

    for(int i=0; i<size;i++)
    {
        if(suspect[i]!=criminal[i])
        {
            match=false;
        }
    }
    if(match==true)
    {
        printf("The two profile match! \n");
    }
    else
    {
        printf("The two profile doesnot match");
    }
    return 0;
}