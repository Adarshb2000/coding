from math import log


class Solution:

    def check(self, r, n):
        return ((r ** n) - 1) // (r - 1) == self.N

    def binary_search(self, n: int):
        answer = -1
        low = 2
        high = self.N

        while low <= high:
            mid = (low + high) // 2
            temp = int(log(self.N, mid))
            if temp == n:
                answer = mid
            if temp < n:
                high = mid - 1
            else:
                low = mid + 1
        
        return answer
                

    def smallestGoodBase(self, n: str):
        self.N = int(n)
        if round(log(self.N + 1, 2), 10).is_integer():
            return '2'
        for n in reversed(range(1, int(log(self.N, 2)) + 1)):
            x = self.binary_search(n)
            if x != -1 and self.check(x, n + 1):
                return x

        return self.N - 1

print(Solution().smallestGoodBase("2251799813685247"))