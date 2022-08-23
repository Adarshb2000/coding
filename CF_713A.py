def cf_713A(numbers: list):
    repeating = 0
    if numbers[0] == numbers[1]:
        repeating = numbers[0]
    
    elif numbers[0] == numbers[2]:
        return 2
    
    elif numbers[1] == numbers[2]:
        return 1
    
    for index, num in enumerate(numbers, start=1):
        if num != repeating:
            return index

if __name__ == '__main__':
    
    for _ in range(int(input())):
        n = int(input())
        numbers = list(map(int, input().split()))
        print(cf_713A(numbers))