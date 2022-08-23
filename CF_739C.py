def cf_739C(k: int):
    square = int(k ** .5)
    sq = square ** 2
    if sq == k:
        return square, 1

    ring = square + 1
    if k - sq <= ring:
        return k - sq, ring
    else:
        return ring, (square + 1) ** 2 - k + 1
    
    
    


if __name__ == '__main__':
    
    for _ in range(int(input())):
        print(*cf_739C(int(input())))