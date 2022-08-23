def cf_753A(letters: str, word: str):
    pos = {}
    for i, l in enumerate(letters):
        pos[l] = i
        
    i = 1
    curr = pos[word[0]]
    answer = 0
    while i < len(word):
        answer += abs(pos[word[i]] - curr)
        curr = pos[word[i]]
        i += 1
    
    return answer

if __name__ == '__main__':
    
    for _ in range(int(input())):
        print(cf_753A(input(), input()))