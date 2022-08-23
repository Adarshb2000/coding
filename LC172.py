class Solution:
    def trailingZeroes(self, n: int):
        temp = 5
        powOf5 = 0
        while n // temp:
            powOf5 += n // temp
            temp *= 5
        
        return powOf5
    
print(Solution().trailingZeroes(6))