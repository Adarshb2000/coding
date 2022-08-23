from math import ceil, log2

def xxoorr(numbers: list[int], k: int):
    max_ = max(numbers)
    if not max_:
        return 0
    bits = ceil(log2(max(numbers)))

    set_bits = [0] * (bits + 1)
    for number in numbers:
        binary = list(map(int, bin(number)[2 :]))
        for index, bit in enumerate(list(reversed(binary))):
            set_bits[-index - 1] += bit

    answer = 0
    for bit in set_bits:
        answer += ceil(bit / k)
    
    return answer




if __name__ == '__main__':
    
    for _ in range(int(input())):
        n, k = map(int, input().split())
        numbers = list(map(int, input().split()))
        print(xxoorr(numbers, k))
