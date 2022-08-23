from math import log2

def irstxor(c):
    x = int(log2(c))

    B = 2 ** x - 1

    A1 = 2 ** x
    
    binary = bin(c)[2 :]

    A2 = 0

    for index, i in enumerate(reversed(binary)):
        if not int(i):
            A2 += 2 ** index

    
    return (A1 + A2) * B
    


if __name__ == '__main__':

    t = int(input())

    while t:

        print(irstxor(int(input())))

        t -= 1