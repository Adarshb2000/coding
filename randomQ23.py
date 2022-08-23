def minTime(numbers1: list, numbers2: list):
    numbers1.sort()
    numbers2.sort(reverse=True)
    if numbers1[-1] > numbers2[0]:
        return 0
    
    answer = [0] * len(numbers2)
    
    while numbers1.__len__():
        curr = numbers1.pop()
        currIndex = 0
        for index, num in enumerate(numbers2):
            if curr > num:
                break
            if answer[index] < answer[currIndex]:
                currIndex = index
            
        answer[currIndex] += 1
    
    return max(answer) * 2 - 1

input()
input()
numbers1 = list(map(int, input().split()))
numbers2 = list(map(int, input().split()))


print(minTime(numbers1, numbers2))