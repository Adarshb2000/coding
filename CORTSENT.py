def getLang(char):
    if 'a' <= char <= 'm':
        return 1
    elif 'N' <= char <= 'Z':
        return 2
    else:
        return 0

def cortsent(words):

    for word in words:
        lang = getLang(word[0])
        if not lang: return False
        for char in word:
            if getLang(char) != lang:
                return False
        
    else:
        return True


if __name__ == '__main__':
    
    for _ in range(int(input())):
        words = input().split()[1 :]
        print('YES' if cortsent(words) else 'NO')