def getFactors(m: int):
    answer = 0
    if m == 1:
        return numbersDict[1]
    for num in numbers:
        if num > m: break
        if num != m and not m % num:
            answer += numbersDict[num]
            
            
    return answer


n = int(input())
numbers = list(map(int, input().split()))
numbersDict = {}
for num in numbers:
    numbersDict[num] = numbersDict.get(num, 0) + 1
# numbers = sorted(numbersDict)

for _ in range(int(input())):
    print(getFactors(int(input())))