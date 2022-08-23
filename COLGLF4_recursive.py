matrix = list()

def recursive(n, eggs, chocolates, omlet, milk, cake, made, omlet_price, milk_price, cake_price):
    global matrix

    if eggs < 0 or chocolates < 0:
        return 10 ** 5
    if made == n:
        return omlet * omlet_price + milk * milk_price + cake * cake_price
    if matrix[omlet][milk][cake]:
        return matrix[omlet][milk][cake]

    matrix[omlet][milk][cake] = min([
        recursive(n, eggs - 2, chocolates, omlet + 1, milk, cake, made + 1, omlet_price, milk_price, cake_price),
        recursive(n, eggs, chocolates - 3, omlet, milk + 1, cake, made + 1, omlet_price, milk_price, cake_price),
        recursive(n, eggs - 1, chocolates - 1, omlet, milk, cake + 1, made + 1, omlet_price, milk_price, cake_price)
    ])

    return matrix[omlet][milk][cake]



def colglf4(inp):
    N, eggs, chocolates, omlet_price, milk_price, cake_price = inp
    if eggs > chocolates and N > chocolates + (eggs - chocolates) // 2:
        return -1
    elif chocolates > eggs and N > eggs + (chocolates - eggs) // 3:
        return -1
    elif chocolates == eggs and N > eggs:
        return -1

    global matrix
    matrix = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(N)]
    
    return recursive(N, eggs, chocolates, 0, 0, 0, 0, omlet_price, milk_price, cake_price)




    
if __name__ == '__main__':
    t = int(input())

    while t:

        print(colglf4(list(map(int, input().split()))))

        t -= 1