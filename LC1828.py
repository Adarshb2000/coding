from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]):
        dist = lambda target, source = [0, 0]: round(((target[0] - source[0]) ** 2 + (target[1] - source[1]) ** 2) ** .5, 3)

        for point in points:
            point.append(dist(point))
        
        points.sort(key=lambda x: x[2])
        answer = []
        for x, y, r in queries:
            minDist = dist([x, y]) - r
            maxDist = dist([x, y]) + r
            answer.append(0)
            minIndex = max(self.lowerBound(points, minDist), 0)
            maxIndex = self.lowerBound(points, maxDist + 0.1)
            if maxIndex == -1:
                maxIndex = len(points) - 1
            

            for i in range(minIndex, maxIndex + 1):
                if dist(points[i], [x, y]) <= r:
                    answer[-1] += 1
        
        return answer
            
    
    def lowerBound(self, numbers, elem):
        answer = -1
        low = 0
        high = len(numbers) - 1
        while low <= high:
            mid = (low + high) // 2
            if numbers[mid][2] == elem:
                answer = mid
                high = mid - 1
            elif numbers[mid][2] < elem:
                answer = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return answer
    
print(Solution().countPoints([[1,3],[3,3],[5,3],[2,2]], [[2,3,1]]))
        