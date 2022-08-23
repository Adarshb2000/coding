from math import inf


def recur(currDigit, currNumber, currSum, reqSum):
    if currSum == reqSum:
        return currNumber
    
    answer = inf
    for i in range(currDigit + 1, 10):
        answer = min(answer, recur(i, currNumber * 10 + i, currSum + i, reqSum))
    
    return answer

def CF811C(number: int):
    return recur(0, 0, 0, number)


if __name__ == '__main__':
    
    for _ in range(int(input())):
        print(CF811C(int(input())))