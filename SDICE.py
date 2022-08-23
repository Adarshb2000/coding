def sdice(n: int):
    top_layer = {
        0 : 0,
        1 : 20,
        2 : 36,
        3 : 51
    }

    x = 1 if n // 4 else 0

    return (44 * (n // 4))  + (4 - (n % 4)) * 4 * x + top_layer[n % 4]


if __name__ == '__main__':
    t = int(input())

    while t:

        print(sdice(int(input())))

        t -= 1