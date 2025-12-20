#include <stdio.h>
#include <stdbool.h>

int main()
{
    int s_sizeR=1,sizeR=3, sizeC=10,match_count=0;
    //Multiple criminal (10 chromosomes)
    float criminals[sizeR][sizeC];
    float suspects[s_sizeR][sizeC];
    bool match;

    //read multiple profile of 10 values
    for(int i=0;i<sizeR;i++)
    {
        printf("Enter the 10 chromosomes of the %d criminal: \n",i+1);
        for(int j=0; j<sizeC;j++)
        {
            scanf("%f",&criminals[i][j]);
        }
        printf("\n");
    }

    for(int i=0;i<s_sizeR;i++)
    {
        printf("Enter the 10 chromosomes of the %d suspect: \n",i+1);
        for(int j=0; j<sizeC;j++)
        {
            scanf("%f",&suspects[i][j]);
        }
        printf("\n");
    }

     
    for(int sus=0;sus<s_sizeR;sus++)
    {
        //for matching chromosome of each suspect with each criminal
        //one suspect 3 criminal
        for(int cri=0;cri<sizeR;cri++)
        {
            match = true;// to check whether the chromosome matches or not
            printf("Checking if suspect %d chromosome matches with %d criminal: \n",sus+1,cri+1);
            for(int chromo=0;chromo<sizeC;chromo++)
            {
                //checkinng if the suspects chromosome matches with criminal
                if(criminals[cri][chromo]!=suspects[sus][chromo])
                {
                    //if matches returns false if any one chromosome didn't matched
                    match = false;
                }
            }
            if(match== false)
            {
                printf("sus %d profile doesnot match \n",sus+1);
            }
            else
            {
                printf("sus %d profile matches with %d criminal!!!\n",sus+1,cri+1);
                //counting total dna matched if returned true
                match_count+=1; 
                //breaks if match found
            }
        }
        printf("\n");
        
    }
    printf("Suspect chromosome matches with %d criminal profile",match_count);

    return 0;
}