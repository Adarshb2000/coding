from math import inf
def cf_731E(n: int, acLocations: list, acTemperatures: list):
    answer = [inf] * n
    temperatures = {}
    for index, temp in zip(acLocations, acTemperatures):
        answer[index - 1] = temp
        temperatures[index] = temp
    
    acLocations.sort()
    
    start = acLocations[0]
    temp = answer[start - 1]
    for i in range(start + 1, n + 1):
        if i in temperatures:
            if i - start + temp > answer[i - 1]:
                start = i
                temp = answer[i - 1]
        
        answer[i - 1] = min(temp + i - start, answer[i - 1])
    
    start = acLocations[-1]
    temp = answer[start - 1]
    
    for i in range(start, 0, -1):
        if i in temperatures:
            if start - i + temp > answer[i - 1]:
                start = i
                temp = answer[i - 1]
        
        answer[i - 1] = min(start - i + temp, answer[i - 1])
        
    return answer


# def bruteCode(n: int, acLocations: list, acTemperatures: list):
#     answer = [inf] * n
    
    
#     for l, t in zip(acLocations, acTemperatures):
#         for i in range(n):
#             answer[i] = min(l - 1 - i + t, answer[i])
    
#     return answer

# def something():
#     from random import randint
#     while True:
#         n = randint(3, 5)
#         k = randint(1, n)
        
#         locations = list(set([randint(1, n) for _ in range(k)]))
#         k = len(locations)
#         temperatures = [randint(1, 10) for _ in range(k)]
#         answer1 = bruteCode(n, locations, temperatures)
#         answer0 = cf_731E(n, locations, temperatures)
        
#         if answer1 != answer0:
#             print(answer0, answer1)
#             print(n)
#             print(locations)
#             print(temperatures)
#             break
            
# something()
# quit()

if __name__ == '__main__':
    
    for _ in range(int(input())):
        input()
        n, k = map(int, input().split())
        acLocations = list(map(int, input().split()))
        acTemperatures = list(map(int, input().split()))
        
        print(*cf_731E(n, acLocations, acTemperatures))