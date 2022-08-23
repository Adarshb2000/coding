from math import inf
from typing import List
from sys import setrecursionlimit
setrecursionlimit(10 ** 6)

class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]):
        self.n = len(students)
        mentorMask = 2 ** self.n - 1
        self.students = students
        self.mentors = mentors
        self.dp = {}
        return self.recur(0, mentorMask)

    def recur(self, student, mentorMask):
        if student == len(self.students):
            return 0

        if (student, mentorMask) in self.dp:
            return self.dp[(student, mentorMask)]

        answer = -inf
        for mentor in range(self.n):
            if not (1 << mentor) & mentorMask: continue
            answer = max(answer, self.recur(student + 1, mentorMask ^ (1 << mentor)) + self.calculateScore(student, mentor))

        self.dp[(student, mentorMask)] = answer
        return answer

    def calculateScore(self, student, mentor):
        return sum(1 - (a ^ b) for a, b in zip(self.students[student], self.mentors[mentor]))


print(Solution().maxCompatibilitySum([[1, 1, 0], [1, 0, 1]],
                                [[1, 0, 0], [0, 0, 1]]))


