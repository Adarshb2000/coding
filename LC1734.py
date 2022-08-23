from typing import List


class Solution:
    def decode(self, encoded: List[int]):
        xorWithFirst = [0]
        for num in encoded:
            xorWithFirst.append(xorWithFirst[-1] ^ num)
        
        n = len(encoded) + 1
        
        allXor = 0
        for i in range(1, n + 1):
            allXor ^= i
        
        allExceptOne = 0
        for num in xorWithFirst:
            allExceptOne ^= num
        
        first = allExceptOne ^ allXor
        
        answer = []
        for num in xorWithFirst:
            answer.append(first ^ num)

        return answer
    
print(Solution().decode([3, 1]))