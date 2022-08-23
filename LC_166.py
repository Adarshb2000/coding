class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int):
        a = numerator
        b = denominator
        poww = 0
        while a < b:
            a *= 10
            poww += 1
        