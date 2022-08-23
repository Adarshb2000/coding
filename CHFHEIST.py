def chfheist(D, d, P, Q):
    if d == D:
        return P * D
    n = D // d
    answer = P * D
    answer += (n * (n - 1) // 2) * Q * d
    answer += (D % d) * (n) * Q

    return answer

if __name__ == '__main__':
    
    for _ in range(int(input())):
        print(chfheist(*list(map(int, input().split()))))