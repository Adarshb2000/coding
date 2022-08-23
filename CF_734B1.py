def cf_734B(string: str):
    counts = {}
    
    for c in string:
        counts[c] = counts.get(c, 0) + 1
    
    extras = answer = 0
    
    for val in counts.values():
        if val > 1:
            answer += 1
        else:
            extras += 1
    
    return answer + extras // 2

if __name__ == '__main__':
    
    for _ in range(int(input())):
        print(cf_734B(input()))