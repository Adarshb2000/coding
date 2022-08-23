def isPalindrome(string: str):
    for i in range(len(string) // 2):
        if string[i] != string[~i]:
            return False

    return True


def spiral2(matrix):
    from collections import deque
    newM = deque()
    for a in matrix:
        newM.append(deque(a))
    arr = []
    while newM and len(arr) != len(matrix) * len(matrix[0]):
        l = newM.popleft()
        while l:
            arr.append(l.popleft())
        for a in newM:
            arr.append(a.pop())
        if newM:
            a = newM.pop()
            while a:
                arr.append(a.pop())
        for a in newM:
            if a: arr.append(a.popleft())

    answer = []
    curr = ''
    for s in arr:
        curr += s
        if len(curr) > 1 and isPalindrome(curr):
            answer.append(curr)
            curr = ''
    if curr: answer.append(curr)
    return answer


def spiral(inarr):
    m = len(inarr)
    n = len(inarr[0])
    count = 0
    i = 0
    j = 0
    row = [0, m - 1]
    col = [0, n - 1]
    spiralString = ''
    while count < m * n:
        while j < col[1] - 1:
            spiralString += inarr[i][j]
            j += 1
            count += 1
        col[1] -= 1
        while i < row[1] - 1:
            spiralString += inarr[i][j]
            i += 1
            count += 1
        row[1] -= 1
        while j > col[0] + 1:
            spiralString += inarr[i][j]
            j -= 1
            count += 1
        col[0] += 1
        while i > row[0] + 1:
            spiralString += inarr[i][j]
            i -= 1
            count += 1
        row[0] += 1
    return spiralString


matrix = []
for _ in range(int(input())):
    matrix.append(input().split(','))

print(*spiral2(matrix), sep=',')