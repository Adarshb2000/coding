from random import randint


class Solution:
    def longNonDecSub(self, nums):
        self.nums = nums
        self.answer = 0
        self.dp = [-1 for _ in range(len(nums))]
        return self.recur(0, -1)

    def recur(self, curr, last):
        if curr == len(self.nums):
            return 0
        ans = self.recur(curr + 1, last)
        if self.nums[curr] >= last:
            if curr + 1 == len(self.nums):
                return 1
            elif self.dp[curr + 1] == -1:
                self.dp[curr + 1] = self.recur(curr + 1, self.nums[curr])
            ans = max(1 + self.dp[curr + 1], ans)
        return ans

    def countMax(self, arr):
        c = dict()
        for i in arr:
            if i in c:
                c[i] += 1
            else:
                c[i] = 1
        return max([c[i] for i in c])


array = [randint(1, 50) for _ in range(50)]
for m in range(1, 10):
    print(Solution().longNonDecSub(array * m))

# is question me apan ko kya karna tha?
# array of length n di hai usko m times repeat karke usme longest non-decreasing sequence nikalna hai.
# 1 < n < 100, m < 10 ** 9
# 100 * 100 = 10000
# time complexity: O(n)
# m < 100 tak directly solve kar sakte hai.
# if m > 100 m = 100, m = 101, dono ka difference lo
