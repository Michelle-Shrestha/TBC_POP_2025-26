#include <stdio.h>

FILE * fp;
int main()
{
    int size = 3,count=0;
    double arr[size],total=0,average=0;
    printf("Enter %d value: ",size);
    for(int i =0;i<size;i++)
    {
        scanf("%lf",&arr[i]);
        total+=arr[i];
    }
    //prompt user of printing values in the array
    printf("The %d values from the array: \n", size);
    //print the value of each element in the array
    for (int i = 0; i < size; i++)
    {
        printf(" %03lf", arr[i]); //print one at a time
        printf("\n");
    }
    average = total/size;
    printf("Average: %.2lf",average);

    for(int i =0;i<size;i++)
    {
        if(arr[i]>average)
        {
            count+=1;
        }
    }
    printf("Number count above average: %d",count);


    return 0;
}