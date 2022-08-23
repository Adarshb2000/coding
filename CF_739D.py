def minEdit(string1: str, string2: str):
    i = 0
    j = 0
    answer = 0
    while i < len(string1) and j < len(string2):
        if string1[i] != string2[j]:
            answer += 1
            i += 1
        else:
            i += 1
            j += 1
    return answer + len(string2) - j + len(string1) - i
            


if __name__ == '__main__':
    
    powerOf2 = [str(2 ** i) for i in range(55)]
    
    for _ in range(int(input())):
        string1 = input()
        print(min([minEdit(string1, string2) for string2 in powerOf2]))