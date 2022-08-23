def cf_702A(numbers: list):
    answer = 0
    for i in range(len(numbers) - 1):
        b, a = sorted([numbers[i], numbers[i + 1]])
        while 2 * b < a:
            b *= 2
            answer += 1
    
    return answer

if __name__ == '__main__':
    
    for _ in range(int(input())):
        n = int(input())
        print(cf_702A(list(map(int, input().split()))))