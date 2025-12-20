#include <stdio.h>

int main()
{
    int total_hours[8],temp_hours[8], temp_emp[8],hours,emp;
    //employees working hours (7days)
    //during initializing values are kept
    int w_hours[8][7]=
    {
        {2,4,3,4,5,8,8},
        {7,3,4,3,3,4,4},
        {3,3,4,3,3,2,2},
        {9,3,4,7,3,4,1},
        {3,5,4,3,6,3,8},
        {3,4,4,6,3,4,4},
        {3,7,4,8,3,8,4},
        {6,3,5,9,2,7,9}
    };

    for (int i=0; i<8;i++)
    {
        for(int j=0; i<7;i++)
        {
            total_hours[i]+=w_hours[i][j];
        }
    }

    //empp with their working hours in descending order
    for(int i=0;i<8;i++)
    {
        if(temp_emp[i]>temp_emp[i+1])
        {
            
        }
        
    }
    
    

    return 0;
}