from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]):
        self.values = {}
        self.graph = defaultdict(list)
        
        for (u, v), value in zip(equations, values):
            self.graph[u].append(v)
            self.graph[v].append(u)
            self.values[(u, v)] = value
            self.values[(v, u)] = 1 / value
        
        answer = []
        for start, end in queries:
            if start not in self.graph or end not in self.graph:
                answer.append(-1)
                continue
            self.visited = set()
            answer.append(self.dfs(start, end))
        
        return answer
        
    def dfs(self, root: int, end: int, val: int = 1):
        if root == end:
            return val
        
        self.visited.add(root)
        
        for node in self.graph[root]:
            if node not in self.visited:
                ans = self.dfs(node, end, val * self.values[(root, node)])
                if ans != -1:
                    return ans
                
        return -1
        
        