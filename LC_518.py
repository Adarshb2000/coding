from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]):
        coins = sorted(coins)

        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        
        return dp.pop()


k = 100
numbers = [1, 99]
print(Solution().change(k, numbers))