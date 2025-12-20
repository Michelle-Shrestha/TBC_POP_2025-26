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
    //cause the variable itself acts as a pointer.
    scanf("%s",str);

    printf("Enter the sentence: ");
    scanf(" %[^\n]",sen); 

    //scanf("%[^\n]%*s",sen);
    // deletes from the memory
    /*
    Scanset is a specifier represented by %[].
    process only those char which are part of scanset
    is case sensitive

    The 1st char of scanset is caret symbol ('^') then the specifier will 
    stop reading from the first occurrence of that char.
    */

    printf("Character: %c\n",ch);
    printf("String: %s\n",str);
    printf("Sentence: %s\n",sen);

    return 0;
}