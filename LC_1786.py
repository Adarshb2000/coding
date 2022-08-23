from typing import List
import heapq
from collections import defaultdict, deque
from math import inf


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)
        for u, v, weight in edges:
            self.graph[u - 1].append([v - 1, weight])
            self.graph[v - 1].append([u - 1, weight])
        self.cost = [-1] * n
        self.dijkstra(n - 1)
        self.dp = {n - 1: 1}
        return self.dfs()

    def dfs(self, root: int = 0):
        if root in self.dp:
            return self.dp[root]

        self.dp[root] = 0
        for node, _ in self.graph[root]:
            if self.cost[node] < self.cost[root]:
                self.dp[root] = (self.dfs(node) + self.dp[root]) % (10**9 + 7)

        return self.dp[root]

    def dijkstra(self, root: int = 0):
        heap = [(0, root)]
        while heap:
            cost, root = heapq.heappop(heap)
            if self.cost[root] != -1:
                continue
            self.cost[root] = cost
            for node, weight in self.graph[root]:
                if self.cost[node] == -1:
                    heapq.heappush(heap, (weight + cost, node))


print(Solution().countRestrictedPaths(
    5, [[1, 2, 3], [1, 3, 3], [2, 3, 1], [1, 4, 2], [5, 2, 2], [3, 5, 1],
        [5, 4, 10]]))
