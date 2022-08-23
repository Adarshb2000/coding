if __name__ == '__main__':
    
    for _ in range(int(input())):
        input()
        startx, starty = map(int, input().split())
        endx, endy = map(int, input().split())
        forbx, forby = map(int, input().split())
        if startx == endx == forbx and max(starty, endy) > forby > min(starty, endy):
            print(2 + abs(starty - endy))
        elif starty == endy == forby and max(startx, endx) > forbx > min(startx, endx):
            print(2 + abs(startx - endx))
        else:
            print(abs(startx - endx) + abs(starty - endy))
        
        