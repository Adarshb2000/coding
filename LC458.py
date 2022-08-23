from math import log, ceil

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        n = minutesToTest / minutesToDie + 1
        return buckets - 2 if n == 1 else ceil(log(buckets, n))
        

print(Solution().poorPigs(1000, 12, 60))