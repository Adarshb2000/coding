from collections import deque, namedtuple
from typing import List
from math import cos, inf
from collections import defaultdict
import heapq


class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]],
                passingFees: List[int]):
        graph = defaultdict(dict)
        n = len(passingFees)
        for u, v, time in edges:
            graph[u][v] = min(time, graph[u].get(v, inf))
            graph[v][u] = min(time, graph[v].get(u, inf))

        heap = [(passingFees[0], 0, maxTime)]
        visited = [0] * n

        while len(heap):
            cost, root, time = heapq.heappop(heap)
            if time < 0:
                continue

            if root == n - 1:
                return cost

            if visited[root] > time:
                continue
            visited[root] = time

            for node, t in graph[root].items():
                heapq.heappush(heap,
                               (cost + passingFees[node], node, time - t))

        return -1


maxTime = 500
edges = [[36, 1, 2], [8, 41, 29], [47, 7, 50], [33, 17, 6], [47, 37, 28],
         [3, 38, 2], [27, 2, 4], [11, 30, 17], [32, 35, 48], [12, 1, 32],
         [7, 27, 6], [7, 4, 25], [15, 8, 11], [2, 17, 50], [7, 45, 14],
         [40, 8, 48], [4, 22, 5], [28, 23, 20], [20, 27, 49], [26, 34, 13],
         [17, 47, 40], [47, 4, 32], [0, 30, 21], [30, 29, 8], [15, 3, 38],
         [4, 3, 39], [22, 16, 46], [47, 10, 13], [42, 23, 30], [34, 0, 13],
         [12, 25, 11], [5, 2, 1], [7, 36, 48], [44, 11, 7], [20, 47, 9],
         [42, 37, 49], [42, 4, 46], [1, 39, 26], [14, 5, 25], [32, 17, 16],
         [22, 7, 25], [3, 22, 36], [49, 8, 46], [16, 20, 6], [16, 21, 32],
         [26, 43, 35], [43, 19, 7], [0, 2, 35], [35, 37, 25], [25, 48, 46],
         [9, 4, 28], [24, 5, 21], [37, 30, 7], [14, 16, 40], [25, 35, 26],
         [49, 38, 1], [24, 13, 36], [27, 6, 8], [10, 3, 37], [23, 13, 26],
         [31, 21, 19], [28, 1, 48], [15, 21, 18], [17, 7, 40], [33, 12, 24],
         [44, 28, 11], [46, 43, 37], [1, 26, 47], [3, 46, 17], [28, 22, 20],
         [8, 34, 3], [18, 6, 2], [38, 16, 30], [17, 38, 20], [12, 10, 26],
         [21, 40, 18], [19, 2, 25], [31, 28, 25], [41, 8, 5], [9, 3, 14],
         [5, 0, 8], [3, 36, 25], [32, 23, 37], [2, 1, 11], [49, 25, 18],
         [33, 24, 48], [42, 28, 25], [4, 40, 47], [37, 11, 23], [37, 46, 45],
         [9, 42, 35], [34, 1, 19], [17, 2, 17], [15, 17, 13], [33, 20, 1],
         [40, 34, 13], [25, 21, 40], [40, 9, 41], [47, 15, 41], [3, 10, 20],
         [33, 35, 47], [22, 8, 37], [35, 40, 34], [29, 38, 34], [37, 15, 17],
         [28, 39, 43], [24, 37, 28], [16, 24, 8], [37, 46, 10], [4, 44, 34],
         [41, 17, 20], [25, 40, 45], [15, 18, 30], [48, 25, 16], [16, 11, 7],
         [16, 1, 34], [19, 44, 11], [37, 7, 14], [11, 49, 5], [29, 32, 3],
         [17, 32, 7], [39, 18, 10], [25, 14, 9], [1, 0, 36], [7, 28, 46],
         [48, 13, 44], [46, 31, 27], [11, 0, 32], [30, 32, 24], [27, 15, 33],
         [20, 19, 43], [16, 8, 6], [28, 21, 43], [13, 33, 14], [3, 2, 45],
         [20, 6, 27], [35, 17, 23], [38, 46, 48], [46, 48, 5], [45, 43, 20],
         [49, 24, 14], [45, 34, 28], [10, 32, 46], [10, 37, 29], [39, 21, 46],
         [34, 25, 22], [6, 11, 3], [0, 34, 19], [6, 20, 3], [33, 0, 44],
         [4, 6, 15], [35, 13, 22], [29, 41, 20], [6, 4, 33], [45, 15, 43],
         [33, 46, 40], [45, 34, 23], [19, 27, 33], [19, 2, 9], [21, 2, 29],
         [14, 25, 15], [37, 44, 34], [16, 41, 41], [18, 3, 18], [46, 32, 13],
         [43, 48, 47], [28, 13, 39], [26, 47, 46], [13, 28, 46], [26, 19, 32],
         [13, 11, 41], [17, 43, 13], [39, 47, 15], [48, 13, 37], [29, 17, 27],
         [35, 33, 29], [24, 37, 19], [43, 22, 49], [40, 5, 33], [23, 24, 34],
         [38, 13, 12], [8, 2, 10], [43, 16, 44], [2, 31, 46], [48, 10, 15],
         [16, 31, 11], [3, 33, 9], [33, 10, 9], [41, 18, 41], [41, 47, 46],
         [10, 44, 6], [27, 38, 45], [42, 28, 2], [19, 9, 30], [21, 32, 26],
         [48, 41, 10], [28, 42, 9], [31, 7, 42], [0, 17, 41], [1, 0, 25],
         [25, 20, 32]]
passingFees = [
    45, 308, 835, 819, 667, 547, 322, 428, 306, 327, 362, 280, 334, 767, 767,
    533, 514, 9, 539, 125, 153, 325, 937, 745, 334, 804, 336, 587, 71, 463,
    287, 492, 466, 935, 373, 950, 760, 994, 390, 836, 911, 948, 81, 945, 593,
    821, 58, 138, 50, 537
]
print(Solution().minCost(maxTime, edges, passingFees))
