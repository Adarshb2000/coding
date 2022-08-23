class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dp = {}
        
        for num in range(lo, hi + 1):
            power = 0
            temp = num
            while num != 1:
                if num in dp:
                    power += dp[num]
                    break
                
                if num & 1:
                    num = 3 * num + 1
                else:
                    num //= 2
                
                power += 1
            dp[temp] = power
        print(dp)
        nums = [(dp[num], num) for num in range(lo, hi + 1)]
        return sorted(nums)[k][1]

print(Solution().getKth(7, 11, 4))