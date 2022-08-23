def cf_731C(numbers1: list, numbers2: list, k: int):
    answer = []
    currentLength = k
    while len(numbers1) or len(numbers2):
        if numbers1 and not numbers1[-1]:
            answer.append(numbers1.pop())
            currentLength += 1
            
        elif numbers2 and not numbers2[-1]:
            answer.append(numbers2.pop())
            currentLength += 1
        
        elif numbers1 and numbers1[-1] <= currentLength:
            answer.append(numbers1.pop())
        
        elif numbers2 and numbers2[-1] <= currentLength:
            answer.append(numbers2.pop())
        
        else:
            return [-1]
    
    return answer


if __name__ == '__main__':
    
    for _ in range(int(input())):
        input()
        k, *_ = map(int, input().split())
        numbers1 = list(map(int, input().split()))
        numbers2 = list(map(int, input().split()))
        numbers1.reverse()
        numbers2.reverse()
        
        print(*cf_731C(numbers1, numbers2, k))