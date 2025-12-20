/**3.2 (Occurrence of max numbers) Write a program that reads integers, finds the largest of
them, and counts its occurrences. Assume that the input ends with number 0. Suppose that
you entered 3 5 2 5 5 5 0; the program finds that the largest is 5 and the occurrence count for
5 is 4*/

#include <stdio.h>

int main()
{ 
    FILE * fp;
    fp = fopen("occurrence.txt","r");
    int size = 10,num[size], largest=num[0];
    int l_occurrence =0;

    if (fp==NULL)
    {
        printf("File doesnot exist");
        return 1;
    }

    //Reading values from file
    for(int i =0;i<size;i++)
    {
        fscanf(fp,"%d",&num[i]);
        //Assuming  input ends with 0 
        //breaks if input is 0 while fetching 
        if(num[i]==0)
        {
            break;
        }
        if (largest<num[i])
        {
            largest = num[i];
        }
    }

    //counting the occurrence of largest number
    for(int j = 0; j<size;j++)
    {
        if(num[j]==0)
        {
            break;
        }
        if(largest== num[j])
        {
            l_occurrence+=1;
        }
    }

    printf("Largest number: %d\n",largest);
    printf("Largest number occurrence: %d\n",l_occurrence);
    fclose(fp);
    return 0;
}