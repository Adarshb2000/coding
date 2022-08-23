from collections import deque

class BFS:
    def printbfs(self, matrix: list[list[int]], start: int = 0):
        n = len(matrix)
        queue = deque([start])
        visited = set()

        while queue.__len__():
            start = queue.popleft()
            if start in visited:
                continue
            
            print(start)
            visited.add(start)

            for i in range(n):
                if matrix[start][i] and i not in visited:
                    queue.append(i)
        



if __name__ == '__main__':
    matrix = [
        [0, 1, 1, 0, 0, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 1, 0, 0, 1, 1],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
    ]
    BFS().printbfs(matrix)