def calculateCubes(N: int):
    for i in range(1, N + 1):
        cubes.add(i ** 3)
        
def cf_702C(n: int):
    for x in cubes:
        if n - x in cubes:
            return True

if __name__ == '__main__':
    cubes = set()
    calculateCubes(10 ** 4)
    for _ in range(int(input())):
        print('YES' if cf_702C(int(input())) else 'NO')