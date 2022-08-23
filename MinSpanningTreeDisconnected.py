class minSpanningTree:
    def solve(self, points: int, adj):
        self.nodes = points
        self.edges = []
        for node1, node2, weight in adj:
            self.edges.append(weight, node1, node2)
        
        self.edges.sort(reverse=True)
        
        self.visited = set()
        return self.MST()
        
    def MST(self):
        answer = 0
        
        while len(self.visited) != self.nodes:
            weight, node1, node2 = self.edges.pop()
            
            if node1 in self.visited and node2 in self.visited:
                continue
            answer += weight
            self.visited.add(node1)
            self.visited.add(node2)
        return answer