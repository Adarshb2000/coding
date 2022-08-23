from collections import defaultdict

a = defaultdict(int)
string = '-+*++-*++-'
n = 2


i = 0
for i in range(len(string) // n):
    c = ''
    for j in range(i * n, i * n + n):
        c += string[j]
    a[c] += 1
    
print(a)

