from collections import defaultdict
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]):
        numbers = self.splitCounts(nums)
        answer = 0
        for n in numbers:
            answer += self.solve(n)
        
        return answer
    
    def solve(self, nums: List[int]):
        last = nums[0]
        slast = 0
        
        for num in nums[1:]:
            if num + slast > last:
                slast, last = last, num + slast
            else:
                slast = last
        return last
    
    def splitCounts(self, nums: List[int]):
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        numbers = []
        last = -1
        for num, count in sorted(counts.items()):
            if num != last + 1:
                numbers.append([num * count])
            else:
                numbers[-1].append(num * count)
            
            last = num
                
            
        return numbers
        
print(Solution().deleteAndEarn([1, 2, 3, 4, 6, 7, 8]))