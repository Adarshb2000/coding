def cf_730B(numbers: list):
    n = len(numbers)
    total = sum(numbers)
    rem = total % n
    return rem * (n - rem)
    
if __name__ == '__main__':
    
    for _ in range(int(input())):
        n = int(input())
        print(cf_730B(list(map(int, input().split()))))