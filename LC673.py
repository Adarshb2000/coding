from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]):
        numbers = [[1, 1] for _ in range(len(nums))]
        numbers[-1] = [1, 1]
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    if numbers[i][0] - 1 == numbers[j][0]:
                        numbers[i][1] += numbers[j][1]
                    elif numbers[i][0] - 1 < numbers[j][0]:
                        numbers[i] = [numbers[j][0] + 1, numbers[j][1]]
        
        MAX = -1
        answer = 0
        for length, count in numbers:
            if length > MAX:
                answer = count
                MAX = length
            elif length == MAX:
                answer += count
        print(numbers)
        return answer


print(Solution().findNumberOfLIS([2,2,2,2,2]))
        