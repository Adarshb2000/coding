#include <stdio.h>
int main()
{
    int a[100],i, n;
    scanf("%d",&n);  //Number of elements of the array is taken from the test case data 
   
   for (i=0; i<n; i++)
    {
        scanf("%d",a+i); // Input the array elements
    }

for(i = 0; i < n; i++)
{
    for(int j = i + 1; j < n; j++)
    {
        if(*(&a[i]) > *(&a[j]))
        {
            int tmp = *(&a[i]);
            *(&a[i]) = *(&a[j]);
            *(&a[j]) = tmp;
        }
    }
}

    for (i=0; i<n; i++)
    {
        printf("%d\n",*(a+i));
    }
    return 0;
}
