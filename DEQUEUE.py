def dequeue(n, m, numbers):
    locations = {i : [m, 0] for i in range(1, n + 1)}
    for index, num in enumerate(numbers):
        if locations[num][0] > index:
            locations[num][0] = index
        if locations[num][1] < index:
            locations[num][1] = index
    


if __name__ == '__main__':
    
    for _ in range(int(input())):
        n, m = map(int, input().split())
        numbers = list(map(int, input().split()))
        print(dequeue(n, m, numbers))