from itertools import permutations

class Solution:
    def countArrangement(self, n: int):
        answer = 0
        for perm in permutations(list(range(1, n + 1)), n):
            for index, num in enumerate(perm, start=1):
                if num % index and index % num:
                    break
            
            else:
                answer += 1
        
        return answer
    
    
for i in range(1, 20):
    print(i, Solution().countArrangement(i))
