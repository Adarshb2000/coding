from typing import List
from collections import defaultdict


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]):
        self.graph = defaultdict(list)
        self.colors = colors
        for u, v in edges:
            self.graph[u].append(v)

        n = len(colors)
        self.dp = {}
        self.processing = set()
        self.answer = 0
        try:
            for i in range(n):
                self.dfs(i, defaultdict(int))
        except Exception as e:
            print(e)
            return -1

        return self.answer

    def dfs(self, root: int, colors: dict):
        if root in self.processing:
            raise Exception(-1)
        colors[self.colors[root]] += 1

        if not self.graph[root]:
            self.answer = max(self.answer, max(colors.values()))
            return

        self.processing.add(root)

        for node in self.graph[root]:
            self.dfs(node, colors.copy())

        self.processing.remove(root)


print(Solution().largestPathValue(
    "eeyyeeyeye",
    [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [4, 6], [5, 7], [6, 8], [8, 9]]))
