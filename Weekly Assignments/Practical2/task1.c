#include <stdio.h>
int main()
{
    char ch;
    char str[100];
    char sen[100];
    printf("Enter the character: ");
    scanf("%c",&ch);

    printf("Enter the string: ");
    // Amper sign & is not used during array of character 
    //cause the variable itself acts as a pinter.
    scanf("%s",str);

    printf("Enter the sentence: ");
    // using scanset"%[^!]" prints the sentence before exclamation mark
    // when user gives exclamation mark, it stops reading and prints everything before exclamation
    scanf("%[^!]s",sen);

    printf("\n%c\n",ch);
    printf("%s",str);
    printf("%s",sen);
    return 0;
}