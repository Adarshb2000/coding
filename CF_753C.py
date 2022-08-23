def cf_753C(numbers: list):
    numbers.sort(reverse=True)
    curr = answer = numbers.pop()
    while len(numbers):
        temp = numbers.pop() - curr
        answer = max(answer, temp)
        curr += temp
    return answer
        

if __name__ == '__main__':
    
    for _ in range(int(input())):
        input()
        print(cf_753C(list(map(int, input().split()))))