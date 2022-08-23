from typing import List
import heapq


class Solution:
    def maxSizeSlices(self, slices: List[int]):
        slicesWithIndex = [(piece, index) for index, piece in enumerate(slices)]
        heapq.heapify(slicesWithIndex)
        
    
    def recur(self, slices: List[int]):
        pass