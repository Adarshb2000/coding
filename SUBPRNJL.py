from math import ceil
from collections import defaultdict as dd

def subprnjl(numbers: list, k: int):
    counts = [dd(int)]
    for num in numbers:
        temp = counts[-1].copy()
        temp[num] += 1
        counts.append(temp)

    n = len(numbers)
    answer = 0

    for start in range(n):
        for end in range(start + 1, n + 1):
            temp = counts[end].copy()
            for key in counts[start]:
                temp[key] -= counts[start][key]
            nums = sorted(temp.items())
            x = nums[ceil(k / ceil(k / (end - start)))]
            if temp[x] in temp and temp[temp[x]]:
                answer += 1

    return answer
    
if __name__ == '__main__':
    
    for _ in range(int(input())):
        _, k = map(int, input().split())
        numbers = list(map(int, input().split()))
        print(subprnjl(numbers, k))