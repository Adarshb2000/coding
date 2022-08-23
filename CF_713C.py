from random import choice, randint


def cf_713C(string: list, ones: int, zeros: int):
    n = len(string)
    total = string.count('?')
    zero = '0'
    one = '1'
    if n == total == 1:
        return one if ones else zero
    i = 0
    j = n - 1
    while i < j:
        if string[i] != string[j]:
            if string[i] == '?':
                string[i] = string[j]
            elif string[j] == '?':
                string[j] = string[i]
            else:
                return -1

            total -= 1

        i += 1
        j -= 1

    temp_0 = string.count(zero)
    temp_1 = string.count(one)

    if not total:
        if temp_0 != zeros or temp_1 != ones:
            return -1
        return ''.join(string)
    
    zeros -= temp_0
    ones -= temp_1
    if zeros < 0 or ones < 0:
        return -1

    if (not total & 1) and (ones & 1 or zeros & 1): 
        return -1

    if n & 1 and string[n // 2 + 1] == '?':
        if zeros & 1:
            string[n // 2 + 1] = zero
            zeros -= 1
        elif ones & 1:
            string[n // 2 + 1] = one
            ones -= 1
        else:
            return -1
        
        if zeros & 1 or ones & 1:
            return -1
        
        total -= 1
    
    for index, val in enumerate(string):
        if val == '?':
            if ones:
                string[index] = one
                string[n - index - 1] = one
                ones -= 2
            elif zeros:
                string[index] = zero
                string[n - index - 1] = zero
                zeros -= 2
            
            else: 
                return -1
    
    return ''.join(string)
            
        
def something():
    while True:
        one = '1'
        zero = '0'
        string = []
        n = randint(2, 10)
        zeros = randint(1, n)
        ones = n - zeros
        for _ in range(n):
            string.append(choice([one, zero, '?']))
        
        
        answer = cf_713C(string.copy(), ones, zeros)
        if answer == -1:
            continue
        if answer.count(zero) != zeros or answer.count(one) != ones:
            print(zeros, ones)
            print(''.join(string))
            print(answer)
            break

        for i in range(n):
            if answer[i] != answer[n - i - 1]:
                print(zeros, ones)
                print(''.join(string))
                print(answer)
                break


if __name__ == '__main__':
    something()
    exit()
    for _ in range(int(input())):
        zeros, ones = map(int, input().split())
        string = list(input())
        print(cf_713C(string, ones, zeros))
