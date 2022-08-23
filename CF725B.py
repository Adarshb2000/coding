def cf725B(numbers: list):
    n = numbers.__len__()
    sum_ = sum(numbers)
    if sum_ % n:
        return -1
    
    target = sum_ // n
    answer = 0
    for num in numbers:
        if num > target:
            answer += 1
    
    return answer

if __name__ == '__main__':
    
    for _ in range(int(input())):
        n = int(input())
        print(cf725B(list(map(int, input().split()))))