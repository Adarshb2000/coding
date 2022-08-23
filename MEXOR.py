from math import log2

for _ in range(int(input())):
    n = int(input())
    if not n: print(1); continue
    if n == 1: print(2); continue
    t = log2(n)
    p = log2(n + 1)
    if p.is_integer():
        print(n + 1)
        continue
    print(n if t.is_integer() else 2 ** int(t))