from itertools import combinations_with_replacement as cr, permutations as pn


k = 12
i = 3
last = 3
while True:
    for numbers in cr(range(1, k + 1), i):
        for perm in pn(numbers, i):
            for i in range(1, i - 1):
                if 2 * perm[i] <= perm[i + 1] + 2 * perm[i - 1]:
                    break
            
            else:
                i += 1
                break

        else:
            break
    else:
        print(i)
        if last == i:
            break
        else:
            last = i
        continue

    break
        
            