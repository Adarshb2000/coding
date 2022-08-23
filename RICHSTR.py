def richstr(string):
    
    if len(string) < 3:
        for _ in range(Q):
            input()
            print('NO')
        return
    
    array = []
    
    for i in range(len(string) - 3):
        array.append(len(set(string[i : i + 3])) < 3)
    
    prefixArr = [0]
    
    for b in array:
        prefixArr.append(prefixArr[-1] + int(b))
    
    prefixArr.append(prefixArr[-1])
    prefixArr.append(prefixArr[-1])
    prefixArr.append(prefixArr[-1])
        
    
    
    for _ in range(Q):
        l, r = map(int, input().split())
        if r - l < 2:
            print('NO')
            continue
        
        if prefixArr[r - 2] - prefixArr[l - 1]:
            print('YES')
        else:
            print('NO')
        


if __name__ == '__main__':
    
    for _ in range(int(input())):
        _, Q = map(int, input().split())
        richstr(input())
