from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def divide(numbers: list):
            n = len(numbers)

            if n == 1:
                return numbers

            return merge(divide(numbers[: n // 2]), divide(numbers[n // 2 :]))

        def merge(numbers1: list, numbers2: list):
            i = j = 0
            n = len(numbers1)
            m = len(numbers2)
            numbers = []

            curr = 0
            while i < n and j < m:
                if numbers1[i][0] <= numbers2[j][0]:
                    numbers.append(numbers1[i])
                    answer[numbers1[i][1]] += curr
                    i += 1
                else:
                    numbers.append(numbers2[j])
                    curr += 1
                    j += 1

            while i < n:
                numbers.append(numbers1[i])
                answer[numbers1[i][1]] += curr
                i += 1

            while j < m:
                numbers.append(numbers2[j])
                j += 1
            
            return numbers
            
        
        numbers = nums
        numbers = [(num, i) for i, num in enumerate(numbers)]
        answer = [0] * len(numbers)
        divide(numbers)
        return answer

print(Solution().countSmaller([2,0,1]))