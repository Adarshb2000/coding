from collections import defaultdict
from sys import setrecursionlimit

setrecursionlimit(10**9)


def solve(N, A, B, land, water):

    waterGraph = defaultdict(list)
    for a, b in water:
        waterGraph[a].append(b)
        waterGraph[b].append(a)

    landGraph = defaultdict(list)

    for a, b in land:
        landGraph[a].append(b)
        landGraph[b].append(a)

    landConnected = getConnectedPoints(N, landGraph)
    waterConnected = getConnectedPoints(N, waterGraph)

    answers = [0] * (N + 1)

    for i in range(1, N + 1):
        if answers[i] != -1:
            if len(landConnected[i].intersection(waterConnected[i])) == 1:
                answers[i] = len(landConnected[i])
            else:
                for j in landConnected[i]:
                    answers[j] = -1

    return max(answers)


def getConnectedPoints(n, graph):
    connectedPoints = {}
    visited = set()

    for i in range(1, n + 1):
        if i not in visited:
            currVisited = set()
            dfs(i, graph, currVisited)
            for j in currVisited:
                connectedPoints[j] = currVisited
                visited.add(j)

    return connectedPoints


def dfs(root, graph, visited):
    visited.add(root)

    for node in graph[root]:
        if node not in visited:
            dfs(node, graph, visited)


from random import randint

while True:
    n = 10**5
    a = randint(0, n)
    b = randint(0, n - a)
    land = set()
    water = set()
    for _ in range(a):
        x = randint(1, n)
        y = randint(1, n)
        while y == x:
            y = randint(1, n)

        land.add(tuple(sorted([x, y])))

    for _ in range(b):
        x = randint(1, n)
        y = randint(1, n)

        while y == x:
            y = randint(1, n)

        water.add(tuple(sorted([x, y])))

    land = list(land)
    water = list(water)
    print('here')
    # print(land)
    # print(water)
    print(solve(n, a, b, land, water))
    print('-' * 100)
    input()
