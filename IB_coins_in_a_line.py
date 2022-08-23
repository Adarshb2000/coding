class Solution:
    	# @param A : list of integers
	# @return an integer
    def maxcoin(self, A):
        self.coins: list[int] = A
        self.dp = {}
        self.prefix = self.prefixSum(A)
        ans = self.recur()
        print(self.dp)
        return ans
    
    def prefixSum(self, numbers):
        prefix_sum = [0]
        for num in numbers:
            prefix_sum.append(prefix_sum[-1] + num)
        
        return prefix_sum

    def recur(self, player: bool = True, start: int = 0, end: int = None):
        if end is None:
            end = len(self.coins) - 1
        
        if start > end: return 0

        self.dp[(start, end)] = max(
            self.coins[start] + self.recur(not player, start + 1, end),
            self.coins[end] + self.recur(not player, start, end - 1),
        )
        
        if player:
            return self.dp[(start, end)]
        
        else:
            return self.prefix[end + 1] - self.prefix[start] - self.dp[(start, end)]

A = [1, 2, 3, 4]
print(Solution().maxcoin(A))