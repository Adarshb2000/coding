from math import inf
from collections import defaultdict as dd
from typing import List

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]):
        self.graph = dd(list)        
        
        for u, v, time in roads:
            self.graph[u].append([v, time])
            self.graph[v].append([u, time])
        
        self.cost = [[0, inf] for _ in range(n)]
        self.cost[0] = [1, 1]
        self.visited = [False] * n
        
        self.dijkstra()
        return self.cost[-1][0] % (10 ** 9 + 7)
    
    def dijkstra(self, root: int = 0, cost: int = 0):
        
        self.visited[root] = True
        
        for node, time in self.graph[root]:
            if self.cost[node][1] < time + cost:
                continue
            elif self.cost[node][1] == time + cost:
                self.cost[node][0] += self.cost[root][0]
            else:
                self.cost[node] = [self.cost[root][0], time + cost]
        
        nexRoot = 0
        currMin = inf
        for index, cost in enumerate(self.cost):
            if self.visited[index]:
                continue
            if cost[1] < currMin:
                nexRoot = index
                currMin = cost[1]
            
        if nexRoot:
            self.dijkstra(nexRoot, currMin)
            
            
            
print(Solution().countPaths(
7,
[[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]))