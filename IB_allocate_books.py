class Solution:
    def lower_bound(self, low, high):
        answer = -1

        while low <= high:
            mid = (low + high) // 2

            if self.check(mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
    
        return answer

    
    def check(self, pages: int):
        curr = 0
        students = 1
        for page in self.books:
            if curr + page <= pages:
                curr += page
            else:
                students += 1
                curr = page
            
            if students > self.students:
                return False
        
        return True

    def books(self, A, B):
        self.books = A
        self.students = B
        return self.lower_bound(max(A), sum(A))
    
print(Solution().books([12, 34, 67, 90], 2))