#include <stdio.h>

int main(int argc, char const *argv[])
{
    int n;
    scanf("%i", &n);
    int answer = 0;
    for (int i = 2; i <= n; i += 1) {
        answer += n / i;
    }
    printf("%i", answer);
    
    return 0;
}
