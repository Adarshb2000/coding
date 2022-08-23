def calculate(a, s):
    na = len(str(a))
    ns = len(str(s))
    b = 0
    count = 0
    if na > ns:
        return -1
    if a > s:
        return -1
    while s > 0:
        ca = a % 10
        cs = s % 10
        if ca <= cs:
            s //= 10
        else:
            cs = s % 100
            if cs - ca > 9:
                return -1
            s //= 100
        if cs - ca < 0:
            return -1
        b = ((10 ** count) * (cs - ca)) + b
        a //= 10
        count += 1
    if a:
        return -1
    else:
        return b
    

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

from random import randint

while True:
    a = randint(1, 10 ** 5)
    s = randint(1, 10 ** 5)
    answer0 = cf_762C(list(str(a)), list(str(s)))
    answer1 = calculate(a, s)
    if answer0 != answer1:
        print(answer0, answer1)
        print(a, s)
        break