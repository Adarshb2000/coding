from math import gcd

def splitMaxLCM(curr: int, gcd1: int, gcd2: int):
    if curr == n:
        return max((gcd1 * gcd2) // gcd(gcd1, gcd2))
    
    if (curr, gcd1, gcd2) in dp:
        return dp[(curr, gcd1, gcd2)]
    elif (curr, gcd2, gcd1) in dp:
        return dp[(curr, gcd2, gcd1)]
    
    
    


n = int(input())
dp = {}
numbers = []
for _ in range(n):
    numbers.append(map(int, input().split()))

splitMaxLCM(numbers)