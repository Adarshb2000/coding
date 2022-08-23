from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]):
        answer = []
        groupSizes = sorted([[size, group] for group, size in enumerate(groupSizes)], reverse=True)
        
        while groupSizes:
            currSize, person = groupSizes.pop()
            currGroup = [person]
            while len(currGroup) != currSize:
                currGroup.append(groupSizes.pop()[1])
            
            answer.append(currGroup)
        
        return answer
        