from typing import List
from collections import defaultdict, deque
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int,
                          dst: int, k: int):
        graph = defaultdict(list)
        for s, d, price in flights:
            graph[s].append((d, price))

        visited = [k] * n

        heap = [(0, src, 0)]

        while len(heap):
            currPrice, root, stops = heapq.heappop(heap)

            if root == dst:
                return currPrice

            if stops > visited[stops]:
                continue

            for node, price in graph[root]:
                heapq.heappush(heap, (price + currPrice, node, stops + 1))

        return -1


n = 3
flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src = 0
dst = 2
k = 1
print(Solution().findCheapestPrice(n, flights, src, dst, k))