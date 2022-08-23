import heapq

def getMinimumHealth(initial_players, new_players, rank):
    curr = [num for num in initial_players]
    heapq.heapify(curr)
    
    while len(curr) > rank:
        heapq.heappop(curr)
    
    answer = curr[0]
    
    for num in new_players:
        heapq.heappush(curr, num)
        heapq.heappop(curr)
        answer += curr[0]
    
    return answer


print(getMinimumHealth([1, 2], [3, 4], 2))
        
    