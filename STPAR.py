def stpar(numbers):
    i = 1
    stack = [2 * len(numbers)]
    for number in numbers:
        if number != i:
            if number > stack[-1]:
                return False
            stack.append(number) 
            i -= 1
        i += 1
        while stack[-1] == i:
            stack.pop()
            i += 1
  
    return True


if __name__ == '__main__':
    n = int(input())
    
    while n:

        print('yes' if stpar(list(map(int, input().split()))) else 'no')
        n = int(input())

