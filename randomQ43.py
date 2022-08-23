from itertools import permutations


def recur(mask, i, matrix):
    pass

def numberOfWays(a, matrix):
    answer = 0
    for perm in permutations(range(a)):
        flag = True
        for index, gift in enumerate(perm):
            if matrix[index][gift] == 3:
                flag = True
                break
            
            elif matrix[index][gift] == 1:
                flag = False
        
        answer += int(flag)
    
    return answer
            

a = int(input())

matrix = []
for _ in range(a):
    matrix.append(list(map(int, input().split())))

print(numberOfWays(a, matrix))