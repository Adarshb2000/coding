class SegmentTree:
    def __init__(self, inputArray: list, func, exclusiveVal):
        from math import ceil, log2
        self.n = len(inputArray)
        self.array = inputArray
        self.func = func
        self.exclusiveVal = exclusiveVal
        self.mapping = {}
        height = ceil(log2(self.n))
        self.segTree = [None] * (2**(height + 1) - 1)
        self.buildTree(0, self.n - 1, 0)

    def buildTree(self, arrLeft, arrRight, segTreeIndex):
        if arrLeft > arrRight:
            return

        elif arrLeft == arrRight:
            self.segTree[segTreeIndex] = {self.array[arrLeft]: 1}
            self.mapping[arrLeft] = segTreeIndex
            return

        mid = (arrLeft + arrRight) // 2
        self.buildTree(arrLeft, mid, 2 * segTreeIndex + 1)
        self.buildTree(mid + 1, arrRight, 2 * segTreeIndex + 2)

        self.segTree[segTreeIndex] = self.func(
            self.segTree[2 * segTreeIndex + 1],
            self.segTree[2 * segTreeIndex + 2])

    def update(self, index, value):
        # self.array[index] = value
        self.segTree[self.mapping[index]] = value
        self.updateTree((self.mapping[index] - 1) // 2)

    def updateTree(self, segTreeIndex):
        self.segTree[segTreeIndex] = self.func(
            self.segTree[2 * segTreeIndex + 1],
            self.segTree[2 * segTreeIndex + 2])
        if not segTreeIndex:
            return
        self.updateTree((segTreeIndex - 1) // 2)

    def query(self, leftIndex, rightIndex):
        return self.queryTree(leftIndex, rightIndex, segRight=self.n - 1)

    def queryTree(self,
                  leftIndex,
                  rightIndex,
                  segLeft=0,
                  segRight=0,
                  segTreeIndex=0):
        if segLeft > segRight:
            return self.exclusiveVal

        if segLeft > rightIndex or segRight < leftIndex:
            return self.exclusiveVal

        if leftIndex <= segLeft <= segRight <= rightIndex:
            return self.segTree[segTreeIndex]

        mid = (segLeft + segRight) // 2
        return self.func(
            self.queryTree(leftIndex, rightIndex, segLeft, mid,
                           2 * segTreeIndex + 1),
            self.queryTree(leftIndex, rightIndex, mid + 1, segRight,
                           2 * segTreeIndex + 2))

    def show(self):
        print(self.segTree)


def func(a, b):
    count = {}

    for key, value in a.items():
        count[key] = count.get(key, 0) + value

    for key, value in b.items():
        count[key] = count.get(key, 0) + value

    return count


def goodString(N, Q, S, arr, ranges):
    segTree = SegmentTree(S, func, {})

    for i, index in enumerate(arr):
        for l, r in ranges:
            counts = set(segTree.query(l - 1, r - 1).values())
            if not (len(counts) == 0 or
                    (len(counts) == 1 and counts.pop() == 1)):
                break
        else:
            return i
        segTree.update(index - 1, {})


from collections import defaultdict


def getCounts(string):
    temp = defaultdict(int)

    for c in string:
        if c.isalpha():
            temp[c] += 1

    return temp


def check(string, ranges):

    for l, r in ranges:
        temp = getCounts(string[l - 1:r])
        counts = set(temp.values())
        if not (len(counts) == 0 or (len(counts) == 1 and counts.pop() == 1)):
            return False
    else:
        return True


def something(N, Q, S, arr, ranges):
    for i, index in enumerate(arr):
        if check(S, ranges):
            return i
        S = list(S)
        S[index - 1] = '_'
        S = ''.join(S)


from string import ascii_lowercase
from random import randint, choice, shuffle

while True:
    N = 10
    string = ''
    for _ in range(N):
        string += choice(ascii_lowercase)
    q = randint(1, 3)
    ranges = []
    for _ in range(q):
        ranges.append((randint(1, N), randint(1, N)))

    arr = list(range(1, N + 1))
    shuffle(arr)
    answer0 = goodString(N, q, string, arr.copy(), ranges.copy())
    answer1 = something(N, q, string, arr.copy(), ranges.copy())
    if answer0 != answer1:
        print(string)
        print(answer0, answer1)
        print(ranges)
        print(arr)
        break

# array = 'adarsh'
# segTree = SegmentTree(array, func, {})
# segTree.show()
# segTree.update(0, {})
# segTree.update(3, {})
# segTree.update(4, {})
# segTree.show()
# print(segTree.query(1, 4))