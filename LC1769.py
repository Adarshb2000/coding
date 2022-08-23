class Solution:
    def minOperations(self, boxes: str):
        currBoxes = 0
        prefix = [0]
        for box in boxes:
            prefix.append(prefix[-1] + currBoxes)
            if box == '1':
                currBoxes += 1
                
        suffix = [0]
        currBoxes = 0
        for box in reversed(boxes):
            suffix.append(suffix[-1] + currBoxes)
            if box == '1':
                currBoxes += 1
        suffix.reverse()
        
        prefix = prefix[1 :]
        suffix = suffix[: -1]
        
        return [p + s for p, s in zip(prefix, suffix)]
        
        
        
Solution().minOperations('010100011001')