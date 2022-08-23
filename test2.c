#include<stdio.h>
#include<stdlib.h>

struct Stack{
    char val;
    struct Stack *next;
};

int main()
{
    int t;
    scanf("%d", &t);
    for(int i = 0; i < t; i++) {
        struct Stack *head;
        char c;
        do {
            scanf("%c", &c);
            if (!head) {
                head = (struct Stack *)malloc(sizeof(struct Stack));
                head->val = c;
                head->next = NULL;
                continue;
            }
            if (c == '+' || c == '-') {
                if (head->val == '<' || head->val == '>' || head->val == '/' || head->val == '*' || head->val == '%' || head->val == '&' || head->val == '=' || head->val == '|' || head->val == '^') {
                    struct Stack *temp = (struct Stack *)malloc(sizeof(struct Stack));
                    temp->val = c;
                    temp->next = head;
                    head = temp;
                    continue;
                }
                struct Stack *ptr = head;
                while(ptr->next && (ptr->next->val == '+' || ptr->next->val == '-')) 
                    ptr = ptr->next;
                struct Stack *temp = (struct Stack *)malloc(sizeof(struct Stack));
                temp->next = ptr->next;
                temp->val = c;
                ptr->next = temp;
            }
            else if(c == '<' || c == '>') {
                if (head->val == '/' || head->val == '*' || head->val == '%' || head->val == '&' || head->val == '=' || head->val == '|' || head->val == '^') {
                    struct Stack *temp = (struct Stack *)malloc(sizeof(struct Stack));
                    temp->val = c;
                    temp->next = head;
                    head = temp;
                    continue;
                }
                struct Stack *s = head;
                while(s->next && (s->next->val == '+' || s->next->val == '-' || s->next->val=='>' || s->next->val=='<')) 
                    s = s->next;
                struct Stack *temp = (struct Stack *)malloc(sizeof(struct Stack));
                temp->next = s->next;
                temp->val = c;
                s->next = temp;
            }
            else if(c == '/' || c == '*' || c == '%') {
                if (head->val == '&' || head->val == '=' || head->val == '|' || head->val == '^') {
                    struct Stack *temp = (struct Stack *)malloc(sizeof(struct Stack));
                    temp->val = c;
                    temp->next = head;
                    head = temp;
                    continue;
                }
                struct Stack *s = head;
                while (s->next && (s->next->val == '+' || s->next->val == '-' || s->next->val=='>' || s->next->val=='<' || s->next->val == '/' || s->next->val == '*' || s->next->val == '%'))
                    s = s->next;
                struct Stack *temp = (struct Stack *)malloc(sizeof(struct Stack));
                temp->next = s->next;
                temp->val = c;
                s->next = temp;  
            }
            else if(c == '=') {
                if (head->val == '&' || head->val == '|' || head->val == '^') {
                    struct Stack *temp = (struct Stack *)malloc(sizeof(struct Stack));
                    temp->val = c;
                    temp->next = head;
                    head = temp;
                    continue;
                }
                struct Stack *s = head;
                while (s->next && (s->next->val == '+' || s->next->val == '-' || s->next->val =='>' || s->next->val =='<' || s->next->val == '/' || s->next->val == '*' || s->next->val == '%' || s->next->val == '=' ))
                    s = s->next;
                struct Stack *temp = (struct Stack *)malloc(sizeof(struct Stack));
                temp->next = s->next;
                temp->val = c;
                s->next = temp; 
            }
            else {
                struct Stack *s = head;
                while (s->next && (s->next->val == '+' || s->next->val == '-' || s->next->val =='>' || s->next->val =='<' || s->next->val == '/' || s->next->val == '*' || s->next->val == '%' || s->next->val == '=' || s->next->val == '&' || s->next->val == '|' || s->next->val == '^'))
                    s = s->next;
                struct Stack *temp = (struct Stack *)malloc(sizeof(struct Stack));
                temp->next = s->next;
                temp->val = c;
                s->next = temp; 
            }
        }
        while(c!='\n');
        struct Stack *s = head;
        while (s) {
            printf("%c ", s->val);
            s = s->next;
        }
    }
    return 0;
}