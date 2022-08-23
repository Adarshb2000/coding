from typing import List
import heapq

class TreeNode:
    def __init__(self, val, index):
        self.val = val
        self.index = index
        self.children = []

class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]):
        
        answer = [1] * len(nums)
        
        if not 1 in nums:
            return answer

        nodes = [TreeNode(val, index) for index, val in enumerate(nums)]
        for index, parent in enumerate(parents):
            if parent == -1: continue
            nodes[parent].children.append(nodes[index])
        
        self.heap = []
        
        curr = 1
        node = nodes[nums.index(1)]
        self.visited = set()
        
        while True:
            self.traverse(node)
            while len(self.heap) and curr <= self.heap[0]:
                heapq.heappop(self.heap)
                curr += 1
                
            answer[node.index] = curr

            if not node.index: break
            node = nodes[parents[node.index]]

        return answer
            
    
    def traverse(self, root: TreeNode):
        if not root or root.val in self.visited:
            return
        
        heapq.heappush(self.heap, root.val)
        
        for child in root.children:
            self.traverse(child)
        
        return
    
print(Solution().smallestMissingValueSubtree([-1,0,1,0,3,3],[5,4,6,2,1,3]))