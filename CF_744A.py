def cf_744A(string: str):
    a = string.count('A') 
    b = string.count('B') 
    c = string.count('C')
    
    return a + c == b

if __name__ == '__main__':
    
    for _ in range(int(input())):
        print('YES' if cf_744A(input()) else 'NO') 