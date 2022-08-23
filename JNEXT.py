def jnext(digits):
    current_max = digits[-1]
    numbers = {i : 0 for i in range(10)}
    n = len(digits) - 1
    while n > -1:
        numbers[digits[n]] += 1
        if digits[n] < current_max:
            break
        else:
            current_max = current_max if current_max > digits[n] else digits[n]
            
        n -= 1
    
    if n == -1:
        return n

    answer = digits[: n]
    for i in range(digits[n] + 1, 10):
        if numbers[i]:
            numbers[i] -= 1
            answer.append(i)
            break
    
    for i in range(10):
        answer += [i] * numbers[i]
    
    final = 0
    for index, digit in enumerate(reversed(answer)):
        final += digit * 10 ** index

    return final

if __name__ == '__main__':
    t = int(input())

    while t:
        input()
        print(jnext(list(map(int, input().split()))))
        
        t -= 1