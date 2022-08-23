from string import ascii_lowercase

def countSubstrings(input_str):
    temp = 'a' + ascii_lowercase
    maps = {}
    for i in range(1, 27):
        maps[temp[i]] = i // 3 + 1

    answer = 0
    
    for start in range(len(input_str)):
        currSum = 0
        for end in range(start, len(input_str)):
            currSum += maps[input_str[end]]
            if currSum % (end - start + 1) == 0:
                answer += 1
        
    
    return answer
        

print(countSubstrings('abcd'))