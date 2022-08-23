def coconut(numbers):
    return numbers[2] // numbers[0] + numbers[3] // numbers[1]

if __name__ == '__main__':
    
    for _ in range(int(input())):
        print(coconut(list(map(int, input().split()))))