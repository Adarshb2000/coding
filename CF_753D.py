def cf_753D(numbers: list, colors: list):
    blues = []
    reds = []
    for num, color in zip(numbers, colors):
        if color == 'B':
            blues.append(num)
        else:
            reds.append(num)
    
    blues.sort(reverse=True)
    reds.sort(reverse=True)
    temp = len(blues)
    for i in range(1, len(blues) + 1):
        num = blues.pop()
        if num < i:
            return False
        
    for i in range(temp + 1, len(numbers) + 1):
        num = reds.pop()
        if num > i:
            return False
        
    return True
        
    

if __name__ == '__main__':
    
    for _ in range(int(input())):
        input()
        print('YES' if cf_753D(list(map(int, input().split())), list(input())) else 'NO')