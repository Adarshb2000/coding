class Solution:
    def getRow(self, rowIndex: int):
        answer = [1]
        for i in range(rowIndex):
            answer.append(answer[-1] * (rowIndex - i) / (i + 1))
        
        return answer

            