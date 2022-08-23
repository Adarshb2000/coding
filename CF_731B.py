def cf_731B(string: str):
    from string import ascii_lowercase
    if 'a' not in string:
        return False

    end = start = string.index('a')
    
    for c in ascii_lowercase[1 : len(string)]:
        if start > 0 and string[start - 1] == c:
            start -= 1
        elif end < len(string) - 1 and string[end + 1] == c:
            end += 1
        else:
            return False
    
    return end - start == len(string) - 1
    
            

if __name__ == '__main__':
    
    for _ in range(int(input())):
        print('YES' if cf_731B(input()) else 'NO')