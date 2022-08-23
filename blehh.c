#include <stdio.h>

int strlen(char input[]) {
    int len = 0;
    while (input[len] != '\0') len += 1;
    return len;
}

int isDigit(char c) {
    return c >= '0' && c <= '9';
}

int isFul(char input[]) {
    return (input[0] == '0' && input[1] == 'x' && input[2] == 'F' && input[3] == 'U' && input[4] == 'L' && input[5] == '\0');
}

long long int convert_from_hexa(char input[]) {
    if (isFul(input)) return 15ll;
    long long result = 0;
    for (int i = 2; input[i] != '\0'; i += 1) {
        result = result << 4;
        if (input[i] >= 'A' && input[i] <= 'F') {
            result += input[i] - 55;
        } else if (isDigit(input[i])) {
            result += input[i] - '0';
        } else {
            return -1;
        }
    }
    return result;
}

long long int convert_from_octa(char input[]) {
    long long int result = 0;
    for (int i = 1; input[i] != '\0'; i += 1) {
        result = result << 3;
        if (isDigit(input[i])) {
            result += input[i] - '0';
        } else {
            return -1;
        }
    }
    return result;
}

long long int convert_from_dec(char input[]) {
    long long int result = 0;
    int end = 0;
    int len = strlen(input);
    if (input[len - 2] == 'U' && input[len - 1] == 'L') {
        end = 2;
    } else if (input[len - 1] == 'L' || input[len - 1] == 'U') {
        end = 1;
    }
    for (int i = 0; i < len - end; i += 1) {
        if (isDigit(input[i])) {
            result = result * 10;
            result += input[i] - '0';
        } else {
            return -1;
        }
    }

    return result;
}

long long int convert_to_decimal(char input[]) {
    switch (type(input)) {
        case 8:
            return convert_from_octa(input);
        case 10:
            return convert_from_dec(input);
        case 16:
            return convert_from_hexa(input);
    }
    return 0;
}

void convert_to_string(long long int number, char string[]) {
    if (number == 0) {
        string[0] = '0';
        string[1] = '\0';
        return;
    }
    int i = 0;
    while (number) {
        string[i++] = number % 10 + '0';
        number /= 10;
    }
    string[i] = '\0';
    strev(string);
    return;
}

int check(char input[]) {

    return 0;
}

int type(char input[]) {
    if (input[0] == '0' && input[1] == 'x') return 16;
    else if (input[0] == '0') return 8;
    else return 10;
}

void strev(char str[])
{
    int len = strlen(str);
    int i;
    for (i = 0; i < len/2; i++)
    {
        char temp = str[i];
        str[i] = str[len-i-1];
        str[len-i-1] = temp;
    }
}

void convert_to_base_i(char input1[], char input2[], int i) {
    long long int num = convert_from_dec(input1);
    if (num == 0) {
        input2[0] = '0';
        input2[1] = '\0';
        return;
    }
    int index = 0;
    while (num > 0) {
        input2[index++] = (num % i) + '0';
        num /= i;
    }
    input2[index] = '\0';
    strev(input2);

    return; 
}

void convert_to_base3(char input1[], char input2[]) {
    convert_to_base_i(input1, input2, 3);
    return;
}

void convert_to_base5(char input1[], char input2[]) {
    convert_to_base_i(input1, input2, 5);
    return;
}

void convert_to_base7(char input1[], char input2[]) {
    convert_to_base_i(input1, input2, 7);
    return;
}

void convert_to_base9(char input1[], char input2[]) {
    convert_to_base_i(input1, input2, 9);
    return;
}

void setValue(char input1[], int i, char input2[]) {
    int len = strlen(input2);
    for (int j = i; j < len + i; j += 1)
        input1[j] = input2[j - i];
    return;
}

void setError(char input1[], long long int num1, long long int num2, char op) {
    char answer[100];
    int curr = 0;


    if (num1 == -1)
    {
        setValue(answer, curr, "(error)");
        answer[7] = op;
        curr = 8;
    } else {
        answer[0] = '(';
        char temp[100];
        convert_to_string(num1, temp);
        int len1 = strlen(temp);
        setValue(answer, 1, temp);
        answer[len1 + 1] = ')';
        answer[len1 + 2] = op;
        curr = len1 + 3;
    }

    if (num2 == -1) {
        setValue(answer, curr, "(error)");
        answer[curr + 7] = '\0';
    } else {
        answer[curr++] = '(';
        char temp[100];
        convert_to_string(num2, temp);
        setValue(answer, curr, temp);
        int len2 = strlen(temp);
        curr += len2;
        answer[curr++] = ')';
        answer[curr] = '\0';
    }
    setValue(input1, 0, answer);
    input1[strlen(answer)] = '\0';
    return;
}

void add(char input1[], char input2[]) {
    long long int num1 = convert_to_decimal(input1);
    long long int num2 = convert_to_decimal(input2);
    if (num1 == -1 || num2 == -1) {
        setError(input1, num1, num2, '+');
        return;
    }
    char temp[100];
    convert_to_string(num1 + num2, temp);
    char answer[100];
    convert_to_base3(temp, answer);
    setValue(input1, 0, answer);
    input1[strlen(answer)] = '\0';
    return;
}

void subtract(char input1[], char input2[]) {
    long long int num1 = convert_to_decimal(input1);
    long long int num2 = convert_to_decimal(input2);
    if (num1 == -1 || num2 == -1) {
        setError(input1, num1, num2, '-');
        return;
    }
    char temp[100];
    convert_to_string(num1 - num2, temp);
    char answer[100];
    convert_to_base3(temp, answer);
    setValue(input1, 0, answer);
    input1[strlen(answer)] = '\0';
    return;
}

void multiply(char input1[], char input2[]) {
    long long int num1 = convert_to_decimal(input1);
    long long int num2 = convert_to_decimal(input2);
    if (num1 == -1 || num2 == -1) {
        setError(input1, num1, num2, '*');
        return;
    }
    char temp[100];
    convert_to_string(num1 * num2, temp);
    char answer[100];
    convert_to_base9(temp, answer);
    setValue(input1, 0, answer);
    input1[strlen(answer)] = '\0';
    return;
}

void divide(char input1[], char input2[]) {
    long long int num1 = convert_to_decimal(input1);
    long long int num2 = convert_to_decimal(input2);
    if (num1 == -1 || num2 == -1) {
        setError(input1, num1, num2, '/');
        return;
    }
    char temp[100];
    convert_to_string(num1 / num2, temp);
    char answer[100];
    convert_to_base5(temp, answer);
    setValue(input1, 0, answer);
    input1[strlen(answer)] = '\0';
    return;
}

void remainder(char input1[], char input2[]) {
    long long int num1 = convert_to_decimal(input1);
    long long int num2 = convert_to_decimal(input2);
    if (num1 == -1 || num2 == -1) {
        setError(input1, num1, num2, '%');
        return;
    }
    char temp[100];
    convert_to_string(num1 % num2, temp);
    char answer[100];
    convert_to_base7(temp, answer);
    setValue(input1, 0, answer);
    input1[strlen(answer)] = '\0';
    return;
}

void calculate(char input1[], char input2[]) {
    char firstString[50], secondString[50];


    int sep = 0;
    while (input1[sep] != ')') sep += 1;

    char op = input1[sep + 1];

    int i, j;
    for (i = 1, j = 0; i < sep; i += 1, j += 1) 
        firstString[j] = input1[i];
    firstString[j] = '\0';

    i = sep + 3;
    j = 0;
    while (input1[i] != ')') {
        secondString[j] = input1[i];
        i += 1;
        j += 1;
    }
    secondString[j] = '\0';


    switch (op) {
        case '+':
            add(firstString, secondString);
            break;
        case '-':
            subtract(firstString, secondString);
            break;
        case '*':
            multiply(firstString, secondString);
            break;
        case '/':
            divide(firstString, secondString);
            break;
        case '%':
            remainder(firstString, secondString);
            break;
    }


    setValue(input2, 0, firstString);
    input2[strlen(firstString)] = '\0';
    return;
}

int main(void) {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i += 1) {
        char input[50];
        scanf("%s", input);
        char answer[50];
        calculate(input, answer);
        printf("%s\n", answer);
    }
}