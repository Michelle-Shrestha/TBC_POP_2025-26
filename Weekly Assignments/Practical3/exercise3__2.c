/**3.2 (Occurrence of max numbers) Write a program that reads integers, finds the largest of
them, and counts its occurrences. Assume that the input ends with number 0. Suppose that
you entered 3 5 2 5 5 5 0; the program finds that the largest is 5 and the occurrence count for
5 is 4*/

#include <stdio.h>

int main()
{ 
    FILE * fp;
    fp = fopen("occurrence.txt","r");
    int num, largest=num, l_occurrence =0,read;

    if (fp==NULL)
    {
        printf("File doesnot exist");
        return 1;
    }
    largest= fscanf(fp,"%d",&num); //suppose the first num is the largest num
    //read checks and stores(in boolean) whether it succeed or failed (does not stores the txt file values /input)
    while((read = fscanf(fp,"%d",&num))!=EOF) 
    {
        //Assuming input ends with 0
        // and when it reaches 0 it breaks the program
        if(num==0)
        {
            break;
        }
        if (largest < num)
        {
            largest = num;
        }
    }
    printf("Largest number: %d\n",largest);
    printf("Largest number occurrence: %d\n",l_occurrence);
    fclose(fp);
    return 0;
}