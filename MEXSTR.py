def mexstr(string):
    n = len(string)
    max_number = n

    zeros = [None] * max_number
    ones = [None] * max_number

    last_pos = -1

    for i in range(n):
        if string[i] == '1':
            for j in range(last_pos + 1, i):
                ones[j] = i
            last_pos = i
    
    for i in range(last_pos + 1, n):
        ones[i] = n
    
    print(ones)
    


    


if __name__ == '__main__':
    t = 1

    while t:

        print(mexstr(input()))

        t -= 1