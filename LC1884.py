class Solution:
    def twoEggDrop(self, n: int):
        # if n < 3: return n
        # dp = [0, 1, 2]
        # for i in range(3, n + 1):
        #     dp.append(min(max(j, dp[i - j] + 1) for j in range(1, i + 1)))

        # return dp[-1]
        
        x = ((8 * n + 1) ** .5 - 1) / 2
        return int(x) if x.is_integer() else int(x) + 1


answers = [0]
for i in range(1, 1001):
    answers.append(Solution().twoEggDrop(i))
    
print(answers)