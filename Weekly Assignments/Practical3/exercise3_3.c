/*3.3 (Count vowels and consonants) Assume letters A, E, I, O, and U as the vowels.
Write a program that prompts the user to enter a string and displays the number of vowels
and consonants in the string.*/

#include <stdio.h>

int main()
{
    int t_vowel=0, t_consonants=0;
    char str[100];
    // To compare sentence with vowel letter
    char vowel[10]= {'a','e','i','o','u','A','E','I','O','U'};
    printf("Enter a word : ");

    // Takes (reads) input until user enters new line.
    scanf("%[^\n]",str); 

    /*loops runs if the string is not null char
    as string ends with null character when it reaches 
    last array(null char) loop ends*/
    for (int i =0; str[i]!='\0';i++)
    {

        //checks whether the given input is alphabet or not
        //done so to not count space in total consonant
        if(str[i]>='A' && str[i]<='Z' || str[i]>='a' && str[i]<='z')
        {
            // the given input is not vowel, resets after each letter
            int is_vowel =0; 
            for(int j =0; j<10;j++)
            {
                if(str[i]==vowel[j])
                {
                    // if the given input is vowel
                    is_vowel =1;
                }
            }
            
            if (is_vowel==1)
            {
                t_vowel+=1;
            }
            if (is_vowel == 0)
            {
                t_consonants+=1;
            }
        }
    }

    printf("\nTotal Vowel: %s",str);
    printf("\nTotal Vowel: %d\n",t_vowel);
    printf("Total Consonants: %d",t_consonants);
    return 0;
}