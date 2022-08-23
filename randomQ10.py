def getMaxTickets(intervals: list):
    low = intervals[0][0]
    high = intervals[0][1]
    
    for l, h in intervals:
        if l > high or h < low:
            return 0
        
        low = max(low, l)
        high = min(high, h)
    
    return high - low + 1


n, m = map(int, input().split())

intervals = []

for _ in range(m):
    intervals.append(list(map(int, input().split())))

print(getMaxTickets(intervals))