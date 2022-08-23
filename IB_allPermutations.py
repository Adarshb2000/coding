class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        self.ans = []
        self.recur(A)
        return self.ans
        

    def recur(self, A: list, nums: list = []):
        if not A:
            self.ans.append(nums)
            return
        
        for index, num in enumerate(A):
            temp = nums.copy()
            temp.append(num)
            self.recur(A[: index] + A[index + 1 :], temp)

