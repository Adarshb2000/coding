class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        row = -1

        low = 0
        high = len(A) - 1

        while low <= high:
            mid = (low + high) // 2
            
            if A[mid][0] > B:
                high = mid - 1
            
            else:
                row = mid
                low = mid + 1

        
        if row == -1:
            return 0
        
        
        elif A[row][0] == B:
            return 1
        
        A = A[row]
        low = 0
        high = len(A[0]) - 1

        while low <= high:
            mid = (low + high) // 2

            if A[mid] == B:
                return 1
            
            elif A[mid] < B:
                low = mid + 1
            
            else:
                high = mid - 1
        
        return 0

A = [
  [3],
  [29],
  [36],
  [63],
  [67],
  [72],
  [74],
  [78],
  [85],
]
B = 41
print(Solution().searchMatrix(A, B))

