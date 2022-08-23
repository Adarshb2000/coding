from collections import deque

def divide(numbers: list):
    if len(numbers) == 1:
        return numbers
    mid = len(numbers) // 2
    return conqure(divide(numbers[: mid]), divide(numbers[mid :]))

def conqure(numbers1: list, numbers2: list):
    global answer
    
    i = j = 0
    n = len(numbers1)
    m = len(numbers2)
    numbers = []
    while i < n and j < m:
        if numbers1[i] > numbers2[j]:
            answer += j
            numbers.append(numbers2[j])
            j += 1
        else:
            numbers.append(numbers1[i])
            i += 1
    
    while i < n:
        answer += j
        numbers.append(numbers1[i])
        i += 1
    
    while j < m:
        numbers.append(numbers2[j])
        j += 1
    
    return numbers
    

def cf_744E(numbers):
    nums = deque()
    for num in numbers:
        if len(nums) and num > nums[0]:
            nums.append(num)
        else:
            nums.appendleft(num)
    
    divide(list(nums))

if __name__ == '__main__':
    
    for _ in range(int(input())):
        input()
        answer = 0
        cf_744E(list(map(int, input().split())))
        print(answer)