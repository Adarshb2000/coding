def subinc(numbers):
    increasings = [1]
    i = 0
    while i < len(numbers) - 1:
        if numbers[i] > numbers[i + 1]:
            increasings.append(1)
        else:
            increasings[-1] += 1
        
        i += 1
    
    return sum([(n * (n + 1)) // 2 for n in increasings])



if __name__ == '__main__':
    for _ in range(int(input())):
        input()
        print(subinc(list(map(int, input().split()))))