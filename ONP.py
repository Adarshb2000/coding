def onp(expression):
    operations = []
    answer = ''
    for i in expression:
        if i == ')':
            answer += operations.pop()
        elif i in ['+', '-', '*', '/', '^']:
            operations.append(i)
        else:
            answer += i
    
    return answer
        


if __name__ == '__main__':
    t = int(input())

    while t:

        print(onp(input()))

        t -= 1