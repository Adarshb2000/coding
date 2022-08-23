class Solution:
    def longestValidParentheses(self, s: str):
        opening = []
        wrongClosing = []

        for index, c in enumerate(s):
            if c == '(':
                opening.append(index)
            elif opening:
                opening.pop()
            else:
                wrongClosing.append(index)

        wrongs = sorted([-1] + opening + wrongClosing) + len(s)
        answer = 0
        for i in range(len(wrongs) - 1):
            answer = max(answer, wrongs[i + 1] - wrongs[i] - 1)

        return answer


s = ')()())'
print(Solution().longestValidParentheses(s))