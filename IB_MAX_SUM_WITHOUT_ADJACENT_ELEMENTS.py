from typing import List


class Solution:
    def adjacent(self, A: List[List[int]]):
        self.n = len(A)
        self.m = len(A[0])

        for i in range(self.n):
            A[i].append(0)
        
        A.append([0] * (self.m + 1))

        self.answer = 0

    def matrix_sum(self, matrix):
        answer = 0
        for row in matrix:
            answer += sum(row)
        
        return answer

    def recur(self, matrix, i = 0, j = 0):
        if i >= self.n and j >= self.m:
            self.answer = max(self.answer, self.matrix_sum(matrix))

        # Inclusion
        temp = matrix.copy()


