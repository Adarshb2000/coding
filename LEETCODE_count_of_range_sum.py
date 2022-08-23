class Solution:
    def countRangeSum(self, nums: list, lower: int, upper: int):
        def divide(self, numbers: list):
            n = len(numbers)
            if n == 1:
                return numbers
            
            return merge(self, divide(self, numbers[: n // 2]), divide(self, numbers[n // 2 :]))

        def merge(self, numbers1: list, numbers2: list):
            
            i = j = 0
            n = numbers1.__len__()
            m = numbers2.__len__()
            numbers = []
            while i < n and j < m:
                if numbers1[i] < numbers2[j]:
                    numbers.append(numbers1[i])
                    i += 1
                else:
                    numbers.append(numbers2[j])
                    j += 1
            
            while i < n:
                numbers.append(numbers1[i])
                i += 1
            
            while j < m:
                numbers.append(numbers2[j])
                j += 1
            
            i = 0
            j = 0
            for num in numbers1:
                while i < m and numbers2[i] - num < self.lower:
                    i += 1
                
                while j < m and numbers2[j] - num <= self.upper:
                    j += 1
                
                self.answer += j - i

            return numbers
        
        self.answer = 0
        self.lower = lower
        self.upper = upper
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        divide(self, prefix_sum)
        return self.answer

print(Solution().countRangeSum([-2,5,-1], -2, 2))