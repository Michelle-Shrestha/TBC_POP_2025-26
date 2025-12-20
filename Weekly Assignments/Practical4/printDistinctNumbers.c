#include <stdio.h>
#include <stdbool.h>

int main()
{
    int size=10, input_num[size], num_count=0, d_num[num_count] ;
    bool dist;

    //taking input
    printf("Enter %d numbers: ",size);
    for(int i=0; i<size; i++)
    {
        scanf("%d",&input_num[i]);
    }

    for(int i=0; i<size; i++)
    {
        dist = true;
        //2nd loop to check if number already presents
        //looping until i's size 
        //(looping with size, it'll always return false cause it'll be comparing all with itself)
        for(int j=0;j<i;j++)
        {
            if(input_num[i]==input_num[j])
            {
                //means there's a duplicate value
                dist=false;
                //if one duplicate value found breaks
                break;
            }
        }

        if (dist==true)
        {
            d_num[num_count]=input_num[i];
            num_count++;
        }

    }

    printf("The number of distinct number: %d\n",num_count);
    printf("The distinct numbers are: ");
    for(int i=0; i<=num_count;i++)
    {
        printf("%d ",d_num[i]);
    }
    
    return 0;
}