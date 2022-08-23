from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]):
        answer = defaultdict(list)
        for string in strs:
            answer[tuple(sorted(string))].append(string)
        
        return list(answer.values())
    
    
    
        