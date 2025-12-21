#include <stdio.h>

int main()
{
    FILE * fp;
    int a,b,c,d;
    fp = fopen("bill_input.txt","r");

    if(fp==NULL)
    {
        printf("File doesnot Exist...");
        return 1;
    }

    printf("Reading Values from bill input \n");
    fscanf(fp,"%d %d %d %d",&a,&b,&c,&d);

    printf("Displaying file: \n");
    printf("%d %d %d %d\n\n",a,b,c,d);
    return 0;
}