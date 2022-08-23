def cf_762B(n):
    answer = 0
    numbers = set()
    for i in [2, 3]:
        x = 1
        while x ** i <= n:
            if x ** i not in numbers:
                answer += 1
                numbers.add(x ** i)
            x += 1
        
    return answer


if __name__ == '__main__':
    
    for _ in range(int(input())):
        print(cf_762B(int(input())))