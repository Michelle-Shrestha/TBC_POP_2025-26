/*Read Values from the Input file*/

#include <stdio.h>

int main()
{
    //file pointer definition to hold a disk location
    FILE * fp;
    fp = fopen("inputFile.txt","r"); 
    //assign its address/disk location to file pointer

    char firstWord[20];
    char secondWord[20];
    int num;

    if(fp==NULL)
    {
        printf("File doesnot Exist...");
        return 1;
    }

    printf("Reads two words and an integer from file \n");
    fscanf(fp,"%s %s %d", firstWord,secondWord,&num);
    
    printf("Display back what has been read from input file: \n");
    printf("%s %s \n%d \n",firstWord,secondWord,num);

    fclose(fp);
    return 0;
}