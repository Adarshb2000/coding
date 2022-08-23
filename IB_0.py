from typing import List


class Solution:
    # @param A : list of strings
	# @return an integer
    def evalRPN(self, A: List[str]):
        stack = []
        operations = {
            '+': int.__add__,
            '-': int.__sub__,
            '*': int.__mul__,
            '/': int.__rfloordiv__
        }

        for c in A:
            if c in operations:
                b = stack.pop()
                a = stack.pop()
                stack.append(operations[c](a, b))
            else:
                stack.append(int(c))
        
        return stack.pop()