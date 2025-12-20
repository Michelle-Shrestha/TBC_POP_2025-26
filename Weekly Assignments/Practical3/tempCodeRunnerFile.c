    //counting the occurrence of largest number
    for(int j = 0; j<size;j++)
    {
        if(num[j]==0)
        {
            break;
        }
        if(largest== num[j])
        {
            l_occurrence+=1;
        }
    }

    printf("Largest number: %d\n",largest);
    printf("Largest number occurrence: %d\n",l_occurrence);
    fclose(fp);
    return 0;
}