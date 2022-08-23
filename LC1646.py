class Solution:
    def getMaximumGenerated(self, n: int):
        if n < 2:
            return n
        numbers = [0] * (n + 1)
        numbers[1] = 1
        for i in range(2, n + 1):
            numbers[i] = numbers[i // 2] + numbers[i // 2 + 1] * (i % 2)
        
        return max(numbers)

for i in range(50):
    print(i, Solution().getMaximumGenerated(i))
                