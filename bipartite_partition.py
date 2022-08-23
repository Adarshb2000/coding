class Solution:
    def solve(self, adj_list):
        self.s1 = set()
        self.s2 = set()
        answer = True
        for start in range(len(adj_list)):
            if start in self.s1 or start in self.s2:
                continue
            answer = answer and self.BFS(adj_list, start)
            if not answer: return answer
            
        return answer
    
    def BFS(self, adj_list: list[list[int]], start: int = 0):
        from collections import deque
        
        queue = deque([(start, True)])
        
        while queue.__len__():
            element, s = queue.popleft()
            
            if s:
                if element in self.s1:
                    continue
                if element in self.s2:
                    return -1
                self.s1.add(element)
            
            else:
                if element in self.s1:
                    return -1
                if element in self.s2:
                    continue
                self.s2.add(element)
            
            for node in adj_list[element]:
                queue.append((node, not s))
        
        return 1

adj_list = {
    0 : [1],
    1 : [2, 4, 6],
    2 : [1, 3],
    3 : [2, 4, 7],
    4 : [1, 3, 5, 7],
    5 : [4, 6],
    6 : [5, 7],
    7 : [3, 4, 6]
}
 
print(Solution().solve(adj_list))           