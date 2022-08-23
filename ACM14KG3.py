from collections import defaultdict as dd
from string import ascii_lowercase

def acm14kg3():
    for index, c in enumerate(s):
        if t[index] not in graph[c]:
            return False
        
    return True


if __name__ == '__main__':
    
    for _ in range(int(input())):
        s = input()
        t = input()
        graph = dd(set)
        for _ in range(int(input())):
            x, y = input().split('->')
            for c in ascii_lowercase:
                if x in graph[c]:
                    graph[c].add(y)
            
            graph[x].add(y)
        
        
        print('YES' if acm14kg3() else 'NO')