from typing import List


class Solution:
    def minSetSize(self, arr: List[int]):
        counts = {}
        for num in arr:
            counts[num] = counts.get(num, 0) + 1

        length = n = len(arr)
        for index, (_, count) in enumerate(sorted(counts.items(), key=lambda x: x[1], reverse=True), start=1):
            length -= count
            if length <= n / 2:
                return index


print(Solution().minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))
