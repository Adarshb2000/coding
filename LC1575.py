from typing import List


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int,
                    fuel: int):
        self.dp = {}
        self.MOD = int(1e9 + 7)
        return self.solve(start, fuel, finish, locations) % self.MOD

    def solve(self, curr, f, end, locations):
        if f < 0:
            return 0

        if (curr, f) in self.dp:
            return self.dp[(curr, f)]

        answer = int(curr == end)
        for index, num in enumerate(locations):
            if index == curr:
                continue
            answer += self.solve(index, f - abs(num - locations[curr]), end,
                                 locations)

        self.dp[(curr, f)] = answer % self.MOD

        return self.dp[(curr, f)]


print(Solution().countRoutes([2,3,6,8,4], 1, 3, 5))