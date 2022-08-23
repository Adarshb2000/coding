from math import log2


class Solution:
    def countBits(self, n: int):
        if n == 0: return [0]
        if n == 1: return [0, 1]
        if n == 2: return [0, 1, 1]
        answer = [None] * (n + 1)
        answer[0] = 0
        answer[1] = 1
        answer[2] = 1
        currPow = 2
        for i in range(3, n + 1):
            if self.isPow2(i):
                answer[i] = 1
                currPow = i
            else:
                answer[i] = answer[i - currPow] + 1

        return answer

    def isPow2(self, n: int):
        return log2(n).is_integer()


print(Solution().countBits(5))