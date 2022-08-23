def cf_713D(numbers: list):
    SUM = sum(numbers)
    uniques = {}
    for num in numbers:
        uniques[num] = uniques.get(num, 0) + 1
    answer = []
    for num in uniques:
        temp = SUM - num
        if not temp & 1:
            temp_sum = temp // 2
            if temp_sum not in uniques:
                continue
            elif temp_sum == num:
                if uniques.get(temp_sum, 0) < 2:
                    continue

            x = num
            SUM = temp // 2
            
            for num in numbers:
                if num == x:
                    x = -1
                    continue
                if num == SUM:
                    SUM = -1
                    continue

                answer.append(num)
    
    return answer if answer else [-1]



if __name__ == '__main__':
    
    for _ in range(int(input())):
        n = int(input())
        numbers = list(map(int, input().split()))
        print(*cf_713D(numbers))