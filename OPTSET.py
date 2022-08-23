from math import log2
from OPTSET_max_xor import get_max_xor

def optset(n, k):

    if log2(n + 1).is_integer():
        if k == n - 3:
            return [*range(1, n - 3), n]
        if k == n - 2:
            answer = set(range(1, n + 1))
            x = 2 ** int(log2(n))
            answer.remove(x)
            answer.remove(x - 1)
            return answer

    if k == 1: return [n]

    elif k == n: return list(range(1, n + 1))

    if log2(n + 2).is_integer():
        if k == n - 1:
            return list(range(2, n + 1))
        elif k == n - 2:
            return [*range(1, n - 2), n]

    if n & 1 and k == n - 1:
        return [*range(1, n - 1), n] if n % 4 == 1 else [*range(1, n)]

    x = 2 ** int(log2(n))
    answer = set()
    if k < x - 1:
        answer.add(x)
        answer.add(x - 1)
        k -= 2
        if k > 3:
            if k < x - 8:
                answer.update(range(x - 5, x - 5 - (k // 4 * 4), -1))
                k %= 4
            else:
                answer.update(range(4, x - 4))
                k -= (x - 8)
        if k == 1:
            answer.remove(x - 1)
            answer.add(x - 2)
            answer.add(1)
        elif k == 2:
            answer.remove(x - 1)
            answer.add(x - 4)
            answer.add(2)
            answer.add(1)
        elif k == 3:
            answer.update([1, 2, 3])
        elif k == 4:
            answer.update([1, 2, x - 2, x - 3])
        return answer

    answer = set([*range(1, x - 1), x])

    if k == x - 1:
        return answer
    
    k -= x - 1
    if k & 1:
        numbers = [*range(x + 1, x + k + 2)]
    else:
        numbers = [*range(x + 1, x + k + 1), x - 1]
    answer.update(numbers)
    curr = 0
    for i in numbers:
        curr ^= i
    answer.remove(curr)
    return answer

    


                


if __name__ == '__main__':
    
    for _ in range(int(input())):
    
        print(optset(*map(int, input().split())))