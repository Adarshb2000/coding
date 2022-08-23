def compiler(string):
    brackets = 0
    opens = []
    for i, bracket in enumerate(string):
        if bracket == '<':
            brackets += 1
            opens.append(i)
        else:
            if brackets:
                brackets -= 1
                opens.pop()
            else:
                return i
    
    if len(opens):
        return opens[0]
    
    return len(string)


if __name__ == '__main__':
    t = int(input())

    while t:

        print(compiler(input()))

        t -= 1


