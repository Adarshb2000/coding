class Solution:
    def solve(self, A: int, B):
        from collections import defaultdict as dd
        self.nodes = A
        self.graph = dd(list)
        min_weight = 1e9
        min_nodes = None
        for node1, node2, weight in B:
            self.graph[node1].append((node2, weight))
            self.graph[node2].append((node1, weight))
            if weight < min_weight:
                min_nodes = [node1, node2]
                min_weight = weight
        
        self.visited = set()
        
        return self.MST(min_nodes[0], min_nodes[1], min_weight)
        
    def MST(self, node1, node2, weight):
        answer = 0
        import heapq
        edges = []
        heapq.heappush(edges, (weight, node1, node2))
        
        
        while len(self.visited) != self.nodes:
            weight, node1, node2 = heapq.heappop(edges)
                    
            if node1 in self.visited and node2 in self.visited:
                continue
            answer += weight
            self.visited.add(node1)
            self.visited.add(node2)
            for node, weight in self.graph[node1]:
                heapq.heappush(edges, (weight, node1, node))

            for node, weight in self.graph[node2]:
                heapq.heappush(edges, (weight, node, node2))
        return answer