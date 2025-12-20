#include <stdio.h>

int main()
{
    int size =10;
    float input_nums[size], mini_num;
    printf("Enter %d numbers: ",size);
    for(int i=0; i<size; i++)
    {
        scanf("%f",&input_nums[i]);
        //supposing mininum number is in index 0
        mini_num=input_nums[0];
    }

    for(int i=0; i<size;i++)
    {
        if(mini_num>input_nums[i])
        {
            mini_num = input_nums[i];
        }
    }

    printf("The minimum number is: %.1f",mini_num);

    return 0;
}