from typing import List


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int):
        if k < 3:
            for _ in range(k - 1):
                arr += arr
        
            return self.kadane(arr)
    
        temp = sum(arr)
        answer = 0
        if temp > 0:
            answer = temp * (k - 2)
            startMax = curr = i = 0
            for index, num in enumerate(arr):
                curr += num
                if curr > startMax:
                    startMax = curr
                    i = index
            
            j = len(arr) - 1
            endMax = curr = 0
            while j > i:
                curr += arr[j]
                endMax = max(curr, endMax)
            
            answer += startMax + endMax
        
        return max(self.kadane(arr * 2), answer)


    def kadane(self, numbers):
        currMax = answer = 0
        
        for num in numbers:
            if currMax <= 0:
                currMax = 0
            
            currMax += num
            
            answer = max(answer, currMax)
        
        
        return answer

print(Solution().kConcatenationMaxSum([]))