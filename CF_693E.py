def correctPlacement(numbers: list):
    smallest = [1e9, 1e9, 0]

    for index, (w, h) in enumerate(numbers):
        if (w < smallest[0] and h < smallest[1]) or (w < smallest[1] and h < smallest[0]):
            smallest = [w, h, index]
    
    answer = []
    for w, h in numbers:
        if (smallest[0] < w and smallest[1] < h) or (smallest[0] < h and smallest[1] < w):
            answer.append(smallest[2] + 1)
        else:
            answer.append(-1)

    return answer

if __name__ == '__main__':
    
    for _ in range(int(input())):
        numbers = []
        for _ in range(int(input())):
            numbers.append(list(map(int, input().split())))
        
        print(*correctPlacement(numbers))