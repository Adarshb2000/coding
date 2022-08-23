class Solution:
    def change(self, amount: int, coins):
        self.answer = 0
        self.amount = amount
        self.coins = sorted(coins)

        self.dp = [0] * (amount + 1)
        self.dp[0] = 1
        for coin in self.coins:
            for i in range(coin, amount + 1):
                self.dp[i] += self.dp[i - coin]
        
        return self.dp.pop()
    
    
n = int(input())
amount = int(input())
numbers = list(map(int, input().split()))
print(Solution().change(amount, numbers))