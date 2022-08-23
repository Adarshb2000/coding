def paparazi_bad(numbers: list):
    answer = 0
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1, i, -1):
            y = lambda x : ((numbers[j] - numbers[i]) * (x - j) / (j - i)) + numbers[j]
            
            alpha = True
            for k in range(i + 1, j):
                if numbers[k] > y(k):
                    alpha = False
                    break

            if not alpha: continue
            elif j - i > answer: answer = j - i; break
            
    return answer


if __name__ == '__main__':
    t = int(input())

    while t:

        input()
        print(paparazi_bad(list(map(int, input().split()))))

        t -= 1