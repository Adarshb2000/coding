def triplets(n, numbers):
    answer = 0
    for i, num in enumerate(numbers):
        j = i + 1
        currJ = numbers[i + 1]
        while j < n:
            if numbers[j] >= num:
                J = j
                break
            currJ = max(currJ, numbers[j])
            j += 1
        else:
            return n - i - 1
        k = J + 1
        currK = numbers[J + 1]
        while k < n:
            if numbers[k] >= currJ:
                K = k
                break
            currK = max(currK, numbers[k])
            k += 1
        else:
            return n - i - 1
        answer = max(K - i, answer)
    
    return answer

n = int(input())
numbers = list(map(int, input().split()))

print(triplets(n, numbers))
            