def lowerBound(elem: int):
    answer = 0
    low = 0
    high = len(sorted_nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_nums[mid] <= elem:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return answer

def minXor(l: int, r: int, x: int):
    i = 0
    start = lowerBound(x)
    xor = -1
    while True:
        if start + i < n + 1:
            num = sorted_nums[start + i]
            if l <= locations[num] <= r:
                xor = num ^ x
        
        if start - i > -1:
            num = sorted_nums[start - i]
            if l <= locations[num] <= r:
                if xor == -1:
                    return locations[sorted_nums[start - i]]
                else:
                    if num ^ x < xor:
                        return locations[sorted_nums[start - i]]
                    else:
                        return locations[sorted_nums[start + i]]
        
        if xor != -1:
            return locations[sorted_nums[start + i]]
        
        i += 1
        
def method1(l, r, x):
    curr_min = 1e9
    curr_index = -1
    for i in range(l, r + 1):
        temp = numbers[i] ^ x
        if temp < curr_min:
            curr_min = temp
            curr_index = i
    
    return curr_index

def something():
    from random import randint, shuffle
    global numbers, sorted_nums, locations, n
    while True:
        numbers = list(set([randint(1, 10) for _ in range(randint(1, 10))]))
        shuffle(numbers)
        numbers = [0] + numbers
        sorted_nums = sorted(numbers)
        locations = {num: i for i, num in enumerate(numbers)}
        
        n = len(numbers) - 1
        l = randint(1, n)
        r = randint(l, n)
        x = randint(1, 10)
        try:
            answer1, answer0 = (method1(l, r, x), minXor(l, r, x))
        except IndexError:
            print(numbers, l, r)
            break
        if answer0 != answer1:
            print(numbers)
            print(l, r)
            print(x)
            print(answer0, answer1)
            break
        else:
            print('Done')

something()
quit()

    

if __name__ == '__main__':
    
    n = int(input())
    for _ in range(n):
        numbers.append(int(input()))
    
    locations = {num: i for i, num in enumerate(numbers)}
    
    sorted_nums = sorted(numbers)

    answer = 0
    X_s = []
    L_s = []
    R_s = []
    q = int(input())
    for _ in range(q):
        X_s.append(int(input()))
    for _ in range(q):
        L_s.append(int(input()))
    for _ in range(q):
        R_s.append(int(input()))
    
    for l, r, x in zip(L_s, R_s, X_s):
        answer += minXor(l, r, x)
    
    print(answer)