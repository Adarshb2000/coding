def one_extended(numbers: list):
    answer = [-1]
    curr = -1
    for index, num in enumerate(numbers, start=1):
        if num == 1:
            curr = index
        
        answer.append(curr)
    
    return answer

def two_contracted(numbers: list):
    answer = [-1] * (len(numbers) + 1)
    curr = -1
    for index in range(len(numbers) - 1, -1, -1):
        if numbers[index] == 2:
            curr = index + 1
        
        answer[index + 1] = curr
    
    return answer

def shroute(trains: list, peeps: list):
    n = trains.__len__()
    m = peeps.__len__()
    ones = one_extended(trains)
    twos = two_contracted(trains)

    answer = [0] * m
    for index, peep in enumerate(peeps):
        if peep == 1:
            continue
        if ones[peep] == twos[peep] == -1:
            answer[index] = -1
        elif ones[peep] == -1:
            answer[index] = twos[peep] - peep
        elif twos[peep] == -1:
            answer[index] = peep - ones[peep]
        else:
            answer[index] = min(twos[peep] - peep, peep - ones[peep])
    
    return answer
        

if __name__ == '__main__':
    
    for _ in range(int(input())):
        input()
        print(*shroute(list(map(int, input().split())), list(map(int, input().split()))))