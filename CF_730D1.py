def cf_730D1(n: int, k: int):
    print(0, flush=True)
    if int(input()):
        return
    
    for i in range(1, n):
        currQ = i ^ (i - 1)
        print(currQ)
        r = int(input())
        if r == 1:
            break
        elif r == -1:
            exit()
        
            
        

if __name__ == '__main__':
    
    for _ in range(int(input())):
        cf_730D1(*map(int, input().split()))