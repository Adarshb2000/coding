def sstacks(n, stacks):
    remainder = 0

    for i, stack in enumerate(stacks):
        if stack >= i:
            remainder += stack - i
        else:
            remainder -= i - stack
            if remainder < 0:
                return False
    
    
    return True



if __name__ == '__main__':
    t = int(input())

    while t:

        print('YES' if sstacks(int(input()), list(map(int, input().split()))) else 'NO')

        t -= 1

