def gameWinner(n: int, numbers: list[int]):
    temp = []
    answer = [0] * n
    numbers = [(index, num) for index, num in enumerate(numbers)]
    level = 0
    while len(numbers) > 1:
        for i in range(0, len(numbers) - 1, 2):
            if numbers[i][1] > numbers[i + 1][1]:
                temp.append(numbers[i])
                answer[numbers[i + 1][0]] = level
            else:
                temp.append(numbers[i + 1])
                answer[numbers[i][0]] = level
        numbers = temp.copy()
        temp = []
        level += 1
    
    answer[numbers.pop()[0]] = level
    return answer

if __name__ == '__main__':
    
    n = 4
    numbers = [1, 4, 3, 2]
    print(gameWinner(n, numbers))            