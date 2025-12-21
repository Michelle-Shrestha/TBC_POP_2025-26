#include <stdio.h>

int main()
{
    int row=3, col=4;
    float matrix[row][col],sum[col];

    printf("Enter a 3-by-4 matrix row by row: \n");
    for(int i=0;i<row;i++)
    {
        for(int j=0; j<col;j++)
        {
            scanf("%f",&matrix[i][j]);
        }
    }

    //looping through columns of rows
    for(int i=0; i<col;i++)
    {
        for(int j=0; j<row;j++)
        {
            //adding the col of the rows
            sum[i]+= matrix[j][i];
        }
    }

    //printing the sum of each column
    for(int i=0;i<col; i++)
    {
        printf("Sum of the elements at column %d is %.1f \n",i,sum[i]);
    }

    return 0;
}