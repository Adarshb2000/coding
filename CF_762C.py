def cf_762C(a: list, s: list):
    b = ''
    while a and s:
        x = int(a.pop())
        if int(s[-1]) < x:
            temp = s.pop()
            if not len(s):
                return -1
            y = int(s.pop() + temp)
        else:
            y = int(s.pop())
        temp = str(y - x)
        if len(temp) != 1:
            return -1
        b += temp
    
    if a:
        return -1
    
    while s:
        b += s.pop()
    answer = ''
    for c in reversed(b):
        answer += c 
    
    return int(answer)


if __name__ == '__main__':
    
    for _ in range(int(input())):
        print(cf_762C(*map(list, input().split())))
        