from collections import defaultdict
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

visited = set()

def getMinTime(n, d, x, y):
    global visited
    visited = set()
    pointsx = defaultdict(list)
    pointsy = defaultdict(list)
    for i, j in zip(x, y):
        pointsx[i].append(j)
        pointsy[j].append(i)
        
    answer = 0
    for i, j in zip(x, y):
        if (i, j) not in visited:
            answer += 1
            dfs(i, j, d, pointsx, pointsy)
    
    return answer    



def dfs(x, y, d, pointsx, pointsy):
    global visited
    if (x, y) in visited:
        return
    visited.add((x, y))
    
    for j in pointsx[x]:
        if j != y and abs(j - y) <= d:
            dfs(x, j, d, pointsx, pointsy)
    
    for i in pointsy[y]:
        if i != x and abs(i - x) <= d:
            dfs(i, y, d, pointsx, pointsy)
            

from random import randint, shuffle
while True:
    temp = 10 ** 9
    n = randint(1, 10 ** 5)
    d = randint(1, temp)
    x = set()
    while len(x) != n:
        x.add(randint(1, temp))
    x = list(x)
    shuffle(x)
    y = set()
    while len(y) != n:
        y.add(randint(1, temp))
    y = list(y)
    shuffle(y)
    print(getMinTime(n, d, x, y))


    
            