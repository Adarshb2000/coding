from typing import List


class Solution:
    def stoneGame(self, piles: List[int]):
        self.dp = {}
        return self.recur(piles, 0, len(piles) - 1)
    
    def recur(self, piles: List[int], start: int, end: int, alice: int = 0, bob: int = 0, turn: int = 1): 
        if start > end:
            return alice > bob
        if (start, end, turn) not in self.dp:
            self.dp[(start, end, turn)] = self.recur(piles, start + 1, end, alice + piles[start] * turn, bob + piles[start] * (1 - turn), 1 - turn) or self.recur(piles, start, end - 1, alice + piles[end] * turn, bob + piles[end] * (1 - turn), 1 - turn)
        return self.dp[(start, end, turn)]

print(Solution().stoneGame([5, 3, 4, 5]))