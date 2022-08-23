from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]):
        nums.sort()
        dp = [[1, -1] for _ in range(len(nums))]
        
        for index, divisor in enumerate(nums):
            for i in range(index + 1, len(nums)):
                if nums[i] % divisor == 0 and dp[i][0] < dp[index][0] + 1:
                    dp[i][0] = dp[index][0] + 1
                    dp[i][1] = index
                
        
        maxLen = max(dp)[0]
        
        i = len(nums) - 1
        while dp[i][0] != maxLen:
            i -= 1
        
        print(dp)
        answer = []
        
        while i != -1:
            answer.append(nums[i])
            i = dp[i][1]
        
        return answer
            
        
        
print(Solution().largestDivisibleSubset([1, 2, 3, 4, 5, 6, 8]))


#  1 2 3 4 5 6 8

#  1 2 2 3 2 3 4
# -1 0 0 1 0 1 3