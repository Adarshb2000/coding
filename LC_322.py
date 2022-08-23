from math import inf
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
            
        
        return dp[-1]
    
coins = [1, 2, 5]
amount = 11
answer = 3
assert(Solution().coinChange(coins, amount) == answer) 