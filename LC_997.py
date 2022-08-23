from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people = {i: set() for i in range(1, n + 1)}
        people2 = {i: set() for i in range(1, n + 1)}

        noTrust = set(range(1, n + 1))
        for a, b in trust:
            people[a].add(b)
            people2[b].add(a)
            noTrust.discard(a)

        if len(noTrust) != 1:
            return -1

        possibleJudge = noTrust.pop()

        return possibleJudge if len(people2[possibleJudge]) == n - 1 else -1