def cf_739E(string: str):
    chars = {}
    removed = ''
    
    totalChars = {}
    for c in string:
        totalChars[c] = totalChars.get(c, 0) + 1
    
    total = len(totalChars)
    
    for c in reversed(string):
        if c not in chars:
            chars[c] = totalChars[c] // total
            total -= 1
            removed += c
            
    removed = removed[:: -1]
    i = 0
    answer = ''
    while len(chars):
        c = string[i]
        chars[c] -= 1
        if not chars[c]:
            del chars[c]
        answer += c
        i += 1
        
    currRemoved = set()
    i = 0
    for r in removed: 
        for c in answer:
            if c not in currRemoved:
                if string[i] == c: 
                    i += 1
                else:
                    return (-1)
        currRemoved.add(r) 
    
    return (answer, removed) if i == len(string) else (-1)




if __name__ == '__main__':
    
    for _ in range(int(input())):
        try:
            print(*cf_739E(input()))
        except Exception as e:
            print(-1)