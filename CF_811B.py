from collections import defaultdict

def CF811B(numbers):
    counts = defaultdict(int)
    bad = set()
    for num in numbers:
        counts[num] += 1
        if counts[num] > 1:
            bad.add(num)
    
    i = 0
    while len(bad) > 0:
        counts[numbers[i]] -= 1
        if counts[numbers[i]] == 1:
            bad.remove(numbers[i])
        
        i += 1
    
    return i


if __name__ == '__main__':
    
    for _ in range(int(input())):
        input()
        print(CF811B(list(map(int, input().split()))))