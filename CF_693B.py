def fairDivision(numbers: list):
    if sum(numbers) % 2: return False
    
    twos = numbers.count(2)
    
    return (not twos % 2) or twos != len(numbers)
    

if __name__ == '__main__':
    
    for _ in range(int(input())):
        input()
        print('YES' if fairDivision(list(map(int, input().split()))) else 'NO')