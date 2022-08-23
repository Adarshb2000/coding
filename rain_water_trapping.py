from typing import List


class Solution:
    def trap(self, height: List[int]):
        if not height:
            return 0
        def MXL(numbers):
            answer = [numbers[0]]
            curr_max = answer[0]
            for num in numbers[1 :]:
                curr_max = max(num, curr_max)
                answer.append(curr_max)
            
            return answer


        def MXR(numbers):
            answer = [numbers[-1]]
            curr_max = answer[0]
            for num in reversed(numbers[: -1]):
                curr_max = max(curr_max, num)
                answer.append(curr_max)
            
            answer.reverse()
            return answer
        
        left = MXL(height)
        right = MXR(height)

        answer = 0

        for index, num in enumerate(height):
            temp = min(left[index], right[index]) - num
            if temp > 0:
                answer += temp
        
        return answer

numbers = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap([4,2,0,3,2,5]))