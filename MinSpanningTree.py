class minSpanningTree:
    def solve(self, points: int, adj):
        from collections import defaultdict as dd
        self.nodes = points
        self.graph = dd(list)
        min_weight = 10 ** 9
        min_nodes = None
        for node1, node2, weight in adj:
            self.graph[node1].append((node2, weight))
            self.graph[node2].append((node1, weight))
            if weight < min_weight:
                min_nodes = [node1, node2]
        
        self.visited = set()
        
        return self.MST(min_nodes[0], min_nodes[1], weight)
        
    def MST(self, node1, node2, weight):
        answer = weight
        import heapq
        edges = []
        
        for node, weight in self.graph[node1]:
            heapq.heappush(edges, (weight, node1, node))

        for node, weight in self.graph[node2]:
            heapq.heappush(edges, (weight, node, node2))
        
        while len(self.visited) != self.nodes:
            weight, node1, node2 = heapq.heappop(edges)
            
            if node1 in self.visited and node2 in self.visited:
                continue
            answer += weight
            self.visited.add(node1)
            self.visited.add(node2)
        return answer