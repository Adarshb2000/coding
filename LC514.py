from collections import defaultdict


class Solution:
    def findRotateSteps(self, ring: str, key: str):
        self.occurrences = defaultdict(list)
        for index, c in enumerate(ring):
            self.occurrences[c].append(index)

        self.dp = {}

        return self.solve(0, 0, key, ring) + len(key)

    def solve(self, keyIndex: int, ringIndex: int, key: str, ring: str):
        if keyIndex == len(key):
            return 0

        if (keyIndex, ringIndex) in self.dp:
            return self.dp[(keyIndex, ringIndex)]

        if ring[ringIndex] == key[keyIndex]:
            self.dp[(keyIndex, ringIndex)] = self.solve(keyIndex + 1, ringIndex, key, ring)
            return self.dp[(keyIndex, ringIndex)]

        array = self.occurrences[key[keyIndex]]
        nearestLeft = self.lowerBound(array, ringIndex)
        nearestRight = self.upperBound(array, ringIndex)

        leftSteps = ringIndex - array[nearestLeft] if nearestLeft != -1 else len(ring) - (array[-1] - ringIndex)
        rightSteps = array[nearestRight] - ringIndex if nearestRight != len(array) else len(ring) - (ringIndex - array[0])

        self.dp[(keyIndex, ringIndex)] = min(
            leftSteps + self.solve(keyIndex + 1, array[nearestLeft], key, ring),
            rightSteps + self.solve(keyIndex + 1, array[nearestRight % len(array)], key, ring)
        )

        return self.dp[(keyIndex, ringIndex)]

    def lowerBound(self, numbers, elem):
        answer = -1
        low = 0
        high = len(numbers) - 1

        while low <= high:
            mid = (low + high) // 2
            if numbers[mid] <= elem:
                answer = mid
                low = mid + 1
            else:
                high = mid - 1

        return answer

    def upperBound(self, numbers, elem):
        answer = len(numbers)
        low = 0
        high = len(numbers) - 1
        while low <= high:
            mid = (low + high) // 2
            if numbers[mid] < elem:
                low = mid + 1
            else:
                answer = mid
                high = mid - 1

        return answer


print(Solution().findRotateSteps('godding', 'ginod'))