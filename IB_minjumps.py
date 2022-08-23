class Solution:
    def jumps(self, A):
        if len(A) == 1:
            return 0
        self.dp = [-1] * len(A)
        self.calculateMinJumps(A, 0)
        return self.dp[0]

    def calculateMinJumps(self, A: list, curr: int):
        
        i = 0
        jumps = 0
        while i < len(A):
            if i + A[i] > len(A) - 1:
                jumps += 1
                break
            max_ = 0
            j = i
            while j <= i + A[i]:
                max_ = max(max_, j + A[j])
            
            i = max_
            



        # if self.dp[curr] != -1:
        #     return self.dp[curr]

        # if curr == len(A) - 1:
        #     return 0
        
        # elif not A[curr]:
        #     return 1e6
        
        # elif curr + A[curr] >= len(A) - 1:
        #     self.dp[curr] = 1
        #     return 1
        
        # temp = 1e6
        # for i in range(curr + 1, curr + A[curr] + 1):
        #     temp = min(temp, 1 + self.calculateMinJumps(A, i))
        
        # self.dp[curr] = temp

        # return temp
    