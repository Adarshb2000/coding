from math import inf


class SegmentTree:
    def __init__(self, inputArray: list, func, exclusiveVal):
        from math import ceil, log2
        self.n = len(inputArray)
        self.array = inputArray
        self.func = func
        self.exclusiveVal = exclusiveVal
        self.mapping = {}
        height = ceil(log2(self.n))
        self.segTree = [None] * (2 ** (height + 1) - 1)
        self.buildTree(0, self.n - 1, 0)

    def buildTree(self, arrLeft, arrRight, segTreeIndex):
        if arrLeft > arrRight:
            return
        
        elif arrLeft == arrRight:
            self.segTree[segTreeIndex] = self.array[arrLeft]
            self.mapping[arrLeft] = segTreeIndex
            return
        
        mid = (arrLeft + arrRight) // 2
        self.buildTree(arrLeft, mid, 2 * segTreeIndex + 1)
        self.buildTree(mid + 1, arrRight, 2 * segTreeIndex + 2)  
        
        self.segTree[segTreeIndex] = self.func(self.segTree[2 * segTreeIndex + 1], self.segTree[2 * segTreeIndex + 2])

    
    def update(self, index, value):
        self.array[index] = value
        self.segTree[self.mapping[index]] = value
        self.updateTree((self.mapping[index] - 1) // 2)
    
    def updateTree(self, segTreeIndex):
        self.segTree[segTreeIndex] = self.func(self.segTree[2 * segTreeIndex + 1], self.segTree[2 * segTreeIndex + 2])
        if not segTreeIndex:
            return
        self.updateTree((segTreeIndex - 1) // 2)
    
    
    def query(self, leftIndex, rightIndex):
        return self.queryTree(leftIndex, rightIndex, segRight=self.n - 1)
    
    def queryTree(self, leftIndex, rightIndex, segLeft = 0, segRight = 0, segTreeIndex = 0):
        if segLeft > segRight:
            return self.exclusiveVal
        
        if segLeft > rightIndex or segRight < leftIndex:
            return self.exclusiveVal
        
        if leftIndex <= segLeft <= segRight <= rightIndex:
            return self.segTree[segTreeIndex]

        mid = (segLeft + segRight) // 2
        return self.func(
            self.queryTree(leftIndex, rightIndex, segLeft, mid, 2 * segTreeIndex + 1), 
            self.queryTree(leftIndex, rightIndex, mid + 1, segRight, 2 * segTreeIndex + 2)
        )
        



def mstick(l: int, r: int):
    MIN = minTree.query(l, r)
    
    return max(maxTree.query(0, l - 1), maxTree.query(r + 1, n - 1), (maxTree.query(l, r) - MIN) / 2) / 1 + MIN


if __name__ == '__main__':
    
    n = int(input())
    numbers = list(map(int, input().split()))
    minTree = SegmentTree(numbers, min, inf)
    maxTree = SegmentTree(numbers, max, -inf)
    
    for _ in range(int(input())):
        print(mstick(*map(int, input().split())))