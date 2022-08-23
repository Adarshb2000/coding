from typing import List


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        oddPrefix = [0]
        evenPrefix = [0]
        oddSum = 0
        evenSum = 0        
        for index, num in enumerate(nums):
            if index & 1:
                oddPrefix.append(oddPrefix[-1] + num)
                evenPrefix.append(evenPrefix[-1])
                oddSum += num
            else:
                oddPrefix.append(oddPrefix[-1])
                evenPrefix.append(evenPrefix[-1] + num)
                evenSum += num

        answer = 0
        for index, num in enumerate(nums):
            currOddPre = oddPrefix[index]
            currEvenPre = evenPrefix[index]
            currOddSuf = oddSum - oddPrefix[index + 1]
            currEvenSuf = evenSum - evenPrefix[index + 1]
            
            if currOddPre + currEvenSuf == currEvenPre + currOddSuf:
                answer += 1

        return answer
print(Solution().waysToMakeFair([1, 2, 3]))
        
                
        