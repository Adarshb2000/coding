from collections import defaultdict
import heapq

def cf_702F(numbers: list):
    nums = defaultdict(int)
    counts = defaultdict(int)
    for num in numbers:
        nums[num] += 1
    
    for values in nums.values():
        counts[values] += 1
    
    greater = n
    less = 0
    
    answer = 10 ** 9
    heap = list(counts.items())
    heapq.heapify(heap)
    while len(heap) and less < answer:
        key, val = heapq.heappop(heap)
        del counts[key]
        
        
if __name__ == '__main__':
    
    for _ in range(int(input())):
        n = int(input())
        print(cf_702F(list(map(int, input().split()))))