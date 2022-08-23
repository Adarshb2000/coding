from math import ceil, log2


class SegmentTree:
    def __init__(self, string: str):
        self.array = []
        chars = {}
        for c in string[: 3]:
            chars[c] = chars.get(c, 0) + 1
        
        self.array.append(len(chars) <= 2)
        for index, char in enumerate(string[3 :]):
            chars[char] = chars.get(char, 0) + 1
            chars[string[index]] -= 1
            if not chars[string[index]]:
                del chars[string[index]]
            
            self.array.append(len(chars) <= 2)
        
        self.n = len(self.array)
        
        self.segTree = [None] * (2 ** ceil(log2(len(self.array)) + 1) - 1)

        self.buildTree(arrRight=len(self.array) - 1)
                
    
    
    def buildTree(self, arrLeft: int = 0, arrRight: int = None, segTreeIndex: int = 0):
            
        if arrLeft > arrRight:
            return
        
        if arrLeft == arrRight:
            self.segTree[segTreeIndex] = self.array[arrRight]
            return
        
        mid = (arrLeft + arrRight) // 2
        self.buildTree(arrLeft, mid, 2 * segTreeIndex + 1)
        self.buildTree(mid + 1, arrRight, 2 * segTreeIndex + 2)
        
        self.segTree[segTreeIndex] = self.segTree[2 * segTreeIndex + 1] or self.segTree[2 * segTreeIndex + 2]
        
    
    def query(self, left: int, right: int):
        if right - left < 2:
            return 0
                
        return self.queryTree(left - 1, right - 1 - 2, arrRight=self.n - 1)
    
    def queryTree(self, queryLeft: int, queryRight: int, arrLeft: int = 0, arrRight: int = None, segIndex: int = 0):
        if arrLeft > arrRight:
            return False
        
        elif arrRight < queryLeft or  queryRight < arrLeft:
            return False
        
        elif queryLeft <= arrLeft <= arrRight <= queryRight:
            return self.segTree[segIndex]
        
        mid = (arrLeft + arrRight) // 2
        left = self.queryTree(queryLeft, queryRight, arrLeft, mid, 2 * segIndex + 1)
        right = self.queryTree(queryLeft, queryRight, mid + 1, arrRight, 2 * segIndex + 2)

        return left or right

if __name__ == '__main__':
    
    for _ in range(int(input())):
        n, q = map(int, input().split())
        string = input()
        segTree = SegmentTree(string)
        for _ in range(q):
            print("YES" if segTree.query(*map(int, input().split())) else "NO")