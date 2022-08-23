from typing import List


class Solution:
    def numTeams(self, rating: List[int]):
        smallsBefore = [0] * len(rating)
        smallsAfter = [0] * len(rating)
        bigsBefore = [0] * len(rating)
        bigsAfter = [0] * len(rating)

        for i, a in enumerate(rating):
            for j, b in enumerate(rating):
                if i > j:
                    if a > b:
                        smallsBefore[i] += 1
                    elif a < b:
                        bigsBefore[i] += 1
                elif i < j:
                    if a > b:
                        smallsAfter[i] += 1
                    elif a < b:
                        bigsAfter[i] += 1
        
        answer = 0
        for a, b in zip(smallsBefore, bigsAfter):
            answer += a * b
        
        for a, b in zip(bigsBefore, smallsAfter):
            answer += a * b
        
        return answer
    
print(Solution().numTeams([2, 5, 3, 4, 1]))
    
                    
        