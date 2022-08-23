from math import inf

class Solution:
    def functions(self, numbers, stops):
        self.dp = {}
        prefix = [0]
        for num in numbers:
            prefix.append(prefix[-1] + num)
        
        answer = self.recur(-1, 0, stops - 1, numbers, prefix)
        return answer

    def recur(self, last, index, stops, numbers, prefix):
        if index == len(numbers):
            return inf if stops else (prefix[index] - prefix[last]) ** 2

        if (last, index, stops) in self.dp:
            return self.dp[(last, index, stops)]

        if last == -1:
            b = inf if not stops else numbers[index]**2 + self.recur(-1, index + 1, stops - 1, numbers, prefix)
            self.dp[(last, index, stops)] = min(self.recur(index, index + 1, stops, numbers, prefix), b)
        
        else:
            b = inf if not stops else (prefix[index + 1] - prefix[last]) ** 2 + self.recur(-1, index + 1, stops - 1, numbers, prefix)
            self.dp[(last, index, stops)] = min(self.recur(last, index + 1, stops, numbers, prefix), b)
        
        return self.dp[(last, index, stops)]







# a = int(input())

numbers = list(map(int, input().split()))
stops = int(input())

print(Solution().functions(numbers, stops))