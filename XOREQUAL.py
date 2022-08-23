
def xorequal(n):
    n -= 1
    if not n: return 1
    modd = 10 ** 9 + 7
    base = 2
    curr = base
    for i in bin(n)[3 :]:
        curr = (curr ** 2) % modd
        if i == '1':
            curr = (curr * base) % modd
    
    return curr

if __name__ == '__main__':
    
    for _ in range(int(input())):
        print(xorequal(int(input())))
            
         