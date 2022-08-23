from math import gcd
import sys
sys.setrecursionlimit(10 ** 6)

def recur(i: int, curr: int, changed: bool):
    global changed_index
    if (i, curr) in dp:
        return dp[(i, curr)]
    if i == n:
        return curr
    new_gcd = gcd(curr, numbers[i])
    if changed:
        return new_gcd if new_gcd == 1 else recur(i + 1, new_gcd, changed)
    
    elif new_gcd == curr:
        return recur(i + 1, curr, changed)
    
    else:
        unchange = recur(i + 1, new_gcd, changed)
        change = recur(i + 1, curr, True)
        if change > unchange:
            changed_index = i
        
        dp[(i, curr)] = ans = max(change, unchange)
        return ans

        

def minnotes(numbers: list):
    global changed_index
    uniques = list(set(numbers))
    if len(uniques) == 1:
        return numbers.__len__()
    temp = numbers.copy()

    denomination = recur(1, numbers[0], False)
    
    if changed_index is None:
        temp[-1] = denomination
    
    else:
        temp[changed_index] = denomination

    a = sum([num // denomination for num in temp])

    changed_index = 0
    denomination = recur(2, numbers[1], True)
    numbers[0] = denomination
    b = sum([num // denomination for num in numbers])

    return min(a, b)





if __name__ == '__main__':

    dp = {}
    changed_index = None
    numbers = sorted(map(int, sys.argv[1 :]))
    n = len(numbers)
    exit(minnotes(numbers))