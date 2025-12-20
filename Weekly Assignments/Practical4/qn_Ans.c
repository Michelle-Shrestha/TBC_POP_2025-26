#include <stdio.h>

int main()
{
    char answers[8][10] = 
            {{'A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'} ,
            {'D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'} ,
            {'E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'},
            {'C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'},
            {'A', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'},
            {'B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'},
            {'B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'},
            {'E', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'}};

    char keys[10] = {'D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D'};
    for(int i=0; i<8; i++)
    {
        int correct_ans =0;
        for(int j=0; j<10; j++)
        {
            //if student answer (col) matches with correct ans (key cols)
            if(answers[i][j]== keys[j])
            {
                correct_ans+=1;
            }
        }
        printf("Student %d's guess %d answer correctly.\n",i+1,correct_ans);
    }
    
    return 0;
}