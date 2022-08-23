from typing import List


class Solution:
    def largestMultipleOfThree(self, digits: List[int]):
        rem = sum(digits) % 3
        counts = { i : 0 for i in range(1, 10)}
        for digit in digits:
            counts[digit] += 1
        
        if rem == 1:
            if counts[1] > 0:
                digits.remove(1)
            elif counts[4] > 0:
                digits.remove(4)
            elif counts[7] > 0:
                digits.remove(7)
            elif counts[2] > 1:
                digits.remove(2) 
                digits.remove(2)
            elif counts[2] > 0 and counts[5] > 0:
                digits.remove(2)
                digits.remove(5)
            elif counts[5] > 1:
                digits.remove(5)
                digits.remove(5)
            elif counts[2] > 0 and counts[8] > 0:
                digits.remove(8)
                digits.remove(2)
            elif counts[5] > 0 and counts[8] > 0:
                digits.remove(8)
                digits.remove(5)
            elif counts[8] > 1:
                digits.remove(8)
                digits.remove(8)
            else:
                return ""
        elif rem == 2:
            if counts[2] > 0:
                digits.remove(2)
            elif counts[5] > 0:
                digits.remove(5)
            elif counts[8] > 0:
                digits.remove(8)
            elif counts[1] > 1:
                digits.remove(1) 
                digits.remove(1)
            elif counts[1] > 0 and counts[4] > 0:
                digits.remove(1)
                digits.remove(4)
            elif counts[4] > 1:
                digits.remove(4)
                digits.remove(4)
            elif counts[1] > 0 and counts[7] > 0:
                digits.remove(7)
                digits.remove(1)
            elif counts[4] > 0 and counts[7] > 0:
                digits.remove(7)
                digits.remove(4)
            elif counts[7] > 1:
                digits.remove(7)
                digits.remove(7)
            else:
                return ""
        
        digits.sort(reverse=True)
        answer = 0
        for digit in digits:
            answer = answer * 10 + digit
        
        return str(answer)
        