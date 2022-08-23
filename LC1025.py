class Solution:
    def divisorGame(self, n: int):
        wins = [False] * (n + 1)
        wins[2] = True
        for i in range(3, n + 1):
            for j in range(1, i):
                if not i % j and wins[j]:
                    wins[i] = True
                    break
        for i, win in enumerate(wins):
            print(i, win)
        return wins.pop()


Solution().divisorGame(100)