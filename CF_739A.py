def cf_739A(k: int):
    i = 1
    while len(answer) < k:
        if i % 3 and i % 10 != 3:
            answer.append(i)
        i += 1

if __name__ == '__main__':
    
    answer = []
    cf_739A(1000)
    for _ in range(int(input())):
        print(answer[int(input()) - 1])