/*
Pseudocode:
1. Begin
2. Define file pointer,and assign address
3. Check if the file is NULL or not
4. Assign Variables
5. Read and take input of suspect dna and criminal from file
6. check if DNA matches or not with file input (listed criminal dna)
7. If matches count the number of time it's matched
8. Print output.
9. Close file.
10.End
*/







#include <stdio.h>
#include<stdbool.h>

int main()
{
    FILE * fp;
    fp = fopen("dna_input.txt","r");

    if (fp==NULL)
    {
        printf("File doesnot exist!!!");
        return 1;
    }

    int cri_sizeR=5,sizec=10, total_match=0;
    float suspect[sizec];
    float criminal[cri_sizeR][sizec];
    bool match;

    //taking input from file of suspect dna
    for(int i=0; i<sizec;i++)
    {
        fscanf(fp,"%f",&suspect[i]);
    }

    //taking input from file of criminal dna
    //printf("Reading criminal dna: ");
    for(int i=0;i<cri_sizeR;i++)
    {
        for(int j=0;j<sizec;j++)
        {
            fscanf(fp,"%f",&criminal[i][j]);
        }
    }

    //checking matching dna 
    for(int cri=0; cri<cri_sizeR;cri++)
    {
        match= true;
        for(int i=0; i<sizec;i++)//runs 10 times
        {
            if(criminal[cri][i]!=suspect[i])
            {
                //if anyone of the dna didn't matched it returns false
                match=false;
            }
        }
        //if matched adds total matched dna 
        if(match==true)
        {
            printf("The suspect dna matches with criminal %d.\n",cri);
            //counts the total matched dna
            total_match+=1;
        }
        /*else
        {
            printf("The suspect dna doesnot matches with criminal %d.\n",cri);
        }*/
        
    }
    printf("Suspect is a repeated offender.\n");
    printf("\nSuspect dna matches with total %d criminals.\n",total_match);
    fclose(fp);
    return 0;
}