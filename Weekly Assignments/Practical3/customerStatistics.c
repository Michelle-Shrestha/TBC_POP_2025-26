/*
Step 1: Start 
Step 2: Open file
Step 3: Take input from the file
Step 4: If about 1000 heave user, 
        else if 500-100 unit consumed regular user 
        below 0-500 unit consumed light user
        else, should enter [positive integer(more than 0)
Step 5: Count the unit consumer 
Step 6: Display the number of consumer, classifiying the users
*/

#include <stdio.h>

int main()
{
    FILE * fp;
    int unit,test_int;
    int count_huser=0, count_ruser=0, count_luser=0;
    fp = fopen("testInput.txt","r");

    if(fp==NULL)
    {
        printf("File doesnot Exist...");
        return 1;
    }
    //takes input from the file unit it reaches the end of file
    
    while((test_int= fscanf(fp,"%d",&unit))!=EOF)
    {
        if (unit>=1000)
        {
            count_huser+=1;
        }
        else if (unit>=500 && unit<1000)
        {
            count_ruser+=1;
        }
        else if (unit>0 && unit<500)
        {
            count_luser+=1;
        }
        else
        {
            printf("Invalid Input!!");
        }
    }
    printf("\nHeavy Users :%d\n",count_huser);
    printf("Regular Users :%d\n",count_ruser);
    printf("Light Users :%d\n",count_luser);

    fclose(fp);
    return 0;
}