def cf725E():
    n = int(input())
    inp = []
    for _ in range(n):
        inp.append(input().split())
    
    variables = {}
    for values in inp:
        if values[1] == ':=':
            variables[values[0]] = values[2]

        else:
            variables[values[0]] = variables[values[2]] + variables[values[4]]
    
    


if __name__ == '__main__':
    
    for _ in range(int(input())):
        print(cf725E())