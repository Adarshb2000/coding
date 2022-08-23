from typing import List

class Solution:
    def NSL(self, heights: List[int]):
        stack = []
        answer = []
        for index, val in enumerate(heights):
            while stack and heights[stack[-1]] >= val:
                stack.pop()
            
            if stack:
                answer.append(stack[-1])
            else:
                answer.append(-1)
            
            stack.append(index)
        
        
        return answer

    def NSR(self, heights: List[int]):
        heights.reverse()
        n = len(heights)

        stack = []
        answer = []
        for index, val in enumerate(heights):
            while stack and heights[stack[-1]] >= val:
                stack.pop()
            
            if stack:
                answer.append(n - stack[-1] - 1)
            else:
                answer.append(n)
            
            stack.append(index)
        
        answer.reverse()
        return answer


    def largestRectangleArea(self, heights: List[int]) -> int:
        left = self.NSL(heights.copy())
        right = self.NSR(heights.copy())

        return max((r - l - 1) * height for l, r, height in zip(left, right, heights))
    
print(Solution().largestRectangleArea([2,1,5,6,2,3]))