// Given a three-digit integer print the sum of its digits.

#include <stdio.h>

int main()
{
    int num,sum=0,temp;
    printf("Enter three digit number: ");
    scanf("%3d",&num);
    if (100<=num && num<=999)
    {
        for(int i =1;i<=3;i++)
        {
            temp=num%10;
            sum = temp+sum;
            num/=10;
        }
        /*It finds and adds(remainder which is last digit) 
        from the last number until the num becomes 0*/
    }
    printf("Sum of three digit number: %d",sum);
    return 0;
}