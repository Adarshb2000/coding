class Solution:
    # @param A : integer
	# @param B : list of integers
	# @param C : list of integers
	# @return an integer
    def solve(self, A, B, C):
        from collections import defaultdict as dd
        self.courses = A
        self.adj_list = dd(list)
        self.completed = [False] * A
        self.process = set()
        
        for req, cor in zip(B, C):
            self.adj_list[cor - 1].append(req - 1)
        
        for course in range(A):
            if self.completed[course]: continue
            if not self.dfs(course):
                return 0
            while len(self.process):
                self.completed[self.process.pop()] = True
        
        return 1
            
    def dfs(self, course: int):
        if self.completed[course]:
            return True
        elif course in self.process:
            return False
        
        self.process.add(course)
        
        answer = True
        for i in self.adj_list[course]:
            answer = answer and self.dfs(i)
            if not answer:
                return False
        self.completed[course] = True
        return True