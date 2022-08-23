import heapq

def evenOddGame(numbers: list):
    A = B = 0
    odds = []
    evens = []
    
    for num in numbers:
        if num % 2:
            heapq.heappush(odds, -num)
        else:
            heapq.heappush(evens, -num)
    
    while odds.__len__() or evens.__len__():
        
        # Alice turn
        maxOdd = 0
        maxEven = 0
        if odds.__len__():
            maxOdd = -odds[0]
        
        if evens.__len__():
            maxEven = -evens[0]
        
        if maxOdd > maxEven:
            heapq.heappop(odds)
        else:
            A -= heapq.heappop(evens)
        
        # Bob turn
        if not (odds.__len__() or evens.__len__()): break
        maxOdd = maxEven = 0
        
        if odds.__len__():
            maxOdd = -odds[0]
        
        if evens.__len__():
            maxEven = -evens[0]
        
        if maxEven > maxOdd:
            heapq.heappop(evens)
        else:
            B -= heapq.heappop(odds)
        
    if A > B:
        return 'Alice'
    elif B > A:
        return 'Bob'
    else:
        return 'Tie'
            
        

if __name__ == '__main__':
    
    for _ in range(int(input())):
        n = int(input())
        print(evenOddGame(list(map(int, input().split()))))