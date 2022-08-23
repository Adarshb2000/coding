def cf_702B(numbers: list):
    n = len(numbers) // 3
    rem = {
        0 : 0,
        1 : 0,
        2 : 0
    }
    extra = rem.copy()

    for num in numbers:
        rem[num % 3] += 1
    answer = 0

    for i in range(3):
        if rem[i] > n:
            extra[i] = rem[i] - n
            rem[i] = n
    
    while not rem[0] == rem[1] == rem[2]:
        for i in range(3):
            if extra[i]:
                rem[(i + 1) % 3] += extra[i]
                answer += extra[i]
                extra[i] = 0
                if rem[(i + 1) % 3] > n:
                    extra[(i + 1) % 3] += rem[(i + 1) % 3] - n
                    rem[(i + 1) % 3] = n
    

    return answer

if __name__ == '__main__':
    
    for _ in range(int(input())):
        input()
        print(cf_702B(list(map(int, input().split()))))