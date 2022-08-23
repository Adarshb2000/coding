def knapSack(strings, val):
    
    weight = [len(string) + 1 for string in strings]
    n = len(weight)
    
    W = 31
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
 
    for i in range(1, n + 1):
        for w in range(1, W + 1):

            if weight[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - weight[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
 
    return K[n][W]

if __name__ == '__main__':
    # n = int(input())
    strings = ['Program', 'Queue', 'stack', 'linked_list', 'update']
    val = [10, 3, 2, 8, 4]
    # strings = []
    # val = []
    # for _ in range(n):
    #     x, y = input().split()
    #     strings.append(x)
    #     val.append(int(y))
        
    print(knapSack(strings, val))
    