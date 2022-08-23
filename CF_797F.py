def CF797F(string, perm):
    new = []
    for index in perm:
        new.append(string[index - 1])
    
    i = 1
    while ''.join(new) != string:
        temp = []
        for index in perm:
            temp.append(new[index - 1])
        
        new = temp
        i += 1
        
    return i    
    
        


for _ in range(int(input())):
    input()
    print(CF797F(input(), list(map(int, input().split()))))