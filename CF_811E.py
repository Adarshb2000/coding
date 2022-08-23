def CF811E(numbers):

    newNumbers = set()
    flag = numbers[-1] % 10 in [0, 5]
    for index, num in enumerate(numbers):
        if num % 10 == 5:
            numbers[index] += 5
            flag = True
            continue
        
        elif num % 10 == 0:
            flag = True
            continue
        
        elif num % 10 not in [2, 4, 6, 8]:
            numbers[index] += num % 10
        
        newNumbers.add(numbers[index] % 20)
        if flag:
            return False
    
    if flag:
        return len(numbers) * min(numbers) == sum(numbers)

    
    cycleOne = set([1, 2, 4, 8, 16])
    cycleTwo = set([3, 6, 12, 14, 18])

    cycle = cycleOne if newNumbers.pop() in cycleOne else cycleTwo
    
    for num in newNumbers:
        if num not in cycle:
            return False
    
    return True
    
    
    
    
    
    



if __name__ == '__main__':
    
    for _ in range(int(input())):
        input()
        print('YES' if CF811E(list(map(int, input().split()))) else 'NO')