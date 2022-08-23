def paparazi(numbers):
    n = len(numbers)
    i = 2

    curr_max = 0
    angle = numbers[1] - numbers[0]
    curr_poss = 0

    temp = 1

    while i < n:
        

        if (numbers[i] - numbers[curr_poss]) / (i - curr_poss) < angle:
            curr_poss = i - 1
            if temp > curr_max: curr_max = temp
            temp = 1
        else:
            temp += 1
        
        if i == n:
            break
        

        angle = (numbers[i] - numbers[curr_poss]) / (i - curr_poss)
        i += 1
    
    if temp > curr_max: curr_max = temp

    return curr_max

if __name__ == '__main__':
    t = int(input())
    while t:

        input()

        print(paparazi(list(map(int, input().split()))))

        t -= 1