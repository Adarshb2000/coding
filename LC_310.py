from typing import List
from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]):
        if n == 1:
            return [0]
        graph = defaultdict(set)
        children = defaultdict(int)
        
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            children[u] += 1
            children[v] += 1
        
        currLeafNode = set()
        for i in range(n):
            if children[i] == 1:
                currLeafNode.add(i)
        
        nextLeafNode = set()
        while len(graph) > 2:
            while currLeafNode:
                node = currLeafNode.pop()
                parent = graph[node].pop()
                graph[parent].remove(node)
                del graph[node]
                children[parent] -= 1
                if children[parent] == 1:
                    nextLeafNode.add(parent)

            while nextLeafNode:
                currLeafNode.add(nextLeafNode.pop())
        
        return list(graph)
    

print(Solution().findMinHeightTrees(
6,
[[0,1],[0,2],[0,3],[3,4],[4,5]]))