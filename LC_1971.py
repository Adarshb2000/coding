from collections import defaultdict as dd, deque
from typing import List
class Solution:
    def bfs(self, n: int, graph: dd, start: int, end: int):
        
        visited = [False] * n
        queue = deque([start])
        
        while len(queue):
            node = queue.popleft()
            print(node)
            visited[node] = True
            
            for i in graph[node]:
                if not visited[i]:
                    if i == end:
                        return True
                    queue.append(i)
        return False
    
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        graph = dd(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        print(graph)
        
        self.bfs(n, graph, start, end)
        
print(Solution().validPath(3,
[[0,1],[1,2],[2,0]],
0,
2))