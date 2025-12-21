#include <stdio.h>

int main()
{
    int total_hours[8]={0},total_emp[8],temp_hours,temp_emp;
    //8 employees working hours (7days)
    //when values are given, it should be done during initialization
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
        for(int j=0; j<7;j++)
        {
            total_hours[i]+=w_hours[i][j];
        }
        //priting emp with working hours
        total_emp[i]=i;
        //printf("Employee %d total working hour: %d\n",i,total_hours[i]);
    }

    printf("\n");
   
    //Ordering empp with their working hours in descending order
    for(int i=0;i<8;i++)
    {
        for(int j =0; j<8;j++)
        {
            if(total_hours[i]>total_hours[j])
            {
                temp_hours = total_hours[j];
                total_hours[j] = total_hours[i];
                total_hours[i]= temp_hours;

                temp_emp=total_emp[j];
                total_emp[j]= total_emp[i];
                total_emp[i]=temp_emp;
            }
        }
    }

    //printing in descending order
    for(int i=0;i<8;i++)
    {
         printf("Employee %d total working hour: %d\n",total_emp[i],total_hours[i]);
    }
    

    return 0;
}