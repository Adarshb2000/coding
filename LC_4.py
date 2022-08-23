from typing import List


class Solution:
    def findMedianSortedArrays(self,
                               nums1: List[int],
                               nums2: List[int],
                               debug: bool = False):
        n = len(nums1)
        m = len(nums2)

        if not (n or m):
            return 0
        if not n:
            if m % 2:
                return nums2[m // 2]
            else:
                return (nums2[m // 2] + nums2[m // 2 - 1]) / 2

        if debug:
            print("debugger on")
            pass

        if not m:
            if n % 2:
                return nums1[n // 2]
            else:
                return (nums1[n // 2] + nums1[n // 2 - 1]) / 2

        start0 = start1 = 0
        end0 = n - 1
        end1 = m - 1

        while (end0 - start0) > 2 and (end1 - start1) > 2:
            mid0 = (start0 + end0) // 2 + 1
            mid1 = (start1 + end1) // 2 + 1

            if nums1[mid0] < nums2[mid1]:
                start0 = mid0
                end1 = mid1

            else:
                end0 = mid0
                start1 = mid1

        final = []
        for i in range(start0, end0 + 1):
            final.append(nums1[i])

        for i in range(start1, end1 + 1):
            final.append(nums2[i])

        final.sort()
        if debug:
            pass

        if (n + m) % 2:
            return final[len(final) // 2]
        else:
            return (final[len(final) // 2] + final[len(final) // 2 - 1]) / 2


def method1(nums1: List[int], nums2: List[int]):
    numbers = sorted(nums1 + nums2)
    if len(numbers):
        if len(numbers) % 2:
            return numbers[len(numbers) // 2]
        else:
            return (numbers[len(numbers) // 2 - 1] +
                    numbers[len(numbers) // 2]) / 2
    else:
        return 0


from random import randint
while True:
    n = randint(0, 5)
    m = randint(0, 5)
    nums1 = sorted(randint(0, 10) for _ in range(n))
    nums2 = sorted(randint(0, 10) for _ in range(m))
    answer0 = Solution().findMedianSortedArrays(nums1, nums2)
    answer1 = method1(nums1, nums2)
    if answer0 != answer1:
        print(answer0, answer1)
        print(*nums1)
        print(*nums2)
        Solution().findMedianSortedArrays(nums1, nums2, True)
