def eita(d: int, x: int, y: int, z: int):
    return max(x * 7, y * d + z * (7 - d))



if __name__ == '__main__':
    
    for _ in range(int(input())):
        print(eita(*map(int, input().split())))