from collections import defaultdict
from math import gcd

class Solution:
    def functions(self, numbers):
        numbers.sort()
        if numbers[0] == 1:
            return 0
        visited = set()
        numbersSet = set(numbers)
        
        MAX = max(numbers)
        self.graph = defaultdict(list)
        for num in numbers:
            if num in visited:
                continue
        
            i = 1
            while num * i <= MAX:
                if num * i in numbersSet:
                    self.graph[num].append(num * i)
                    self.graph[num * i].append(num)
                    visited.add(num)
                i += 1
        
        self.visited = set()
        self.dfs(numbers[0])
        
        return int(len(self.visited) == len(numbers))

    def dfs(self, root = 0):

        self.visited.add(root)
        
        for num in self.graph[root]:
            if not num in self.visited:
                self.dfs(num)
            
        
class Solution2:
    def functions(self, numbers):
        if len(numbers) == 1:
            return 1
        if 1 in numbers:
            return False
        self.graph = defaultdict(list)
        for num1 in numbers:
            for num2 in numbers:
                if gcd(num1, num2) > 1:
                    self.graph[num1].append(num2)
        
        self.visited = set()
        
        self.dfs(numbers[0])

        return int(len(self.visited) == len(numbers))
    
    def dfs(self, root = 0):
    
        self.visited.add(root)
        
        for num in self.graph[root]:
            if not num in self.visited:
                self.dfs(num)
    
from random import randint
while True:
    n = 5
    numbers = [randint(1, 100) for _ in range(n)]
    answer0 = Solution().functions(numbers)
    answer1 = Solution2().functions(numbers)
    if answer0 != answer1:
        print(numbers)
        print(answer0, answer1)
        break