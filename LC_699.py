from typing import List
from math import ceil, log2

class SegmentTree:
    def __init__(self, length: int):
        self.n = length
        self._segTreeLength = 2 ** (ceil(log2(self.n)) + 1) - 1
        self._segTree = [0] * self._segTreeLength
        self._lazyTree = [0] * self._segTreeLength
    

    def update(self, updateLeft: int, updateRight: int, value: int):
        maximum = self.query(updateLeft, updateRight)
        self._updateTree(updateLeft, updateRight, maximum + value)
    
    def _updateTree(self, updateLeft: int, updateRight: int, value: int, arrLeft: int = 0, arrRight: int = None, treeIndex: int = 0):
        if arrRight is None:
            arrRight = self.n - 1
        
        if arrLeft > arrRight:
            return
        
        if self._lazyTree[treeIndex]:
            self._segTree[treeIndex] = self._lazyTree[treeIndex]
            if arrLeft != arrRight:
                self._lazyTree[2 * treeIndex + 1] = self._lazyTree[treeIndex]
                self._lazyTree[2 * treeIndex + 2] = self._lazyTree[treeIndex]
            
            self._lazyTree[treeIndex] = 0
            
        
        if updateLeft > arrRight or updateRight < arrLeft:
            return
        
        if updateLeft <= arrLeft <= arrRight <= updateRight:
            self._segTree[treeIndex] = value
            if arrLeft != arrRight:
                self._lazyTree[2 * treeIndex + 1] = value
                self._lazyTree[2 * treeIndex + 2] = value
            return

        mid = (arrLeft + arrRight) // 2
        self._updateTree(updateLeft, updateRight, value, arrLeft, mid, 2 * treeIndex + 1),
        self._updateTree(updateLeft, updateRight, value, mid + 1, arrRight, 2 * treeIndex + 2)
        self._segTree[treeIndex] = max(self._segTree[2 * treeIndex + 1], self._segTree[2 * treeIndex + 2])
    
    def query(self, queryLeft: int, queryRight: int):
        return self._query(queryLeft, queryRight)
    
    def _query(self, queryLeft: int, queryRight: int, arrLeft: int = 0, arrRight: int = None, treeIndex: int = 0):
        if arrRight is None:
            arrRight = self.n - 1
            
        if arrLeft > arrRight:
            return -1
        
        if self._lazyTree[treeIndex]:
            self._segTree[treeIndex] = self._lazyTree[treeIndex]
            if arrLeft != arrRight:
                self._lazyTree[2 * treeIndex + 1] = self._lazyTree[treeIndex]
                self._lazyTree[2 * treeIndex + 2] = self._lazyTree[treeIndex]
            
            self._lazyTree[treeIndex] = 0
        
        if arrRight < queryLeft or arrLeft > queryRight:
            return -1
        
        if queryLeft <= arrLeft <= arrRight <= queryRight:
            return self._segTree[treeIndex]
        
        mid = (arrLeft + arrRight) // 2
        
        return max(
            self._query(queryLeft, queryRight, arrLeft, mid, 2 * treeIndex + 1),
            self._query(queryLeft, queryRight, mid + 1, arrRight, 2 * treeIndex + 2)
        )
        
    
    def getMax(self):
        return self._segTree[0]            

class Solution:
    def fallingSquares(self, positions: List[List[int]]):
        segTree = SegmentTree(8)
        answer = []
        for start, size in positions:
            segTree.update(start, start + size - 1, size)
            answer.append(segTree.getMax())
        
        return answer
    

print(Solution().fallingSquares([[0, 2], [1, 3], [5, 1]]))