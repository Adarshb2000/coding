from math import log2

def get_max_xor(n, k):
    if k == 1: return n
    elif k == n:
        x = n % 4
        if x == 0: return n
        if x == 1: return 1
        if x == 2: return n + 1
        if x == 3: return 0
    
    a = log2(n)
    if a.is_integer():
        return 2 * n - 1

        

    a = int(a)

    if k < n - 2:
        return 2 ** (a + 1) - 1
    
    if log2(n + 2).is_integer():
        return n
    
    elif n % 2 and k == n - 1:
        return n
    
    else:
        return 2 ** (a + 1) - 1



        
# def something():
#     for n in range(1, 1000):
#         for k in range(1, n + 1):
#             answer1 = get_max_xor(n, k)
#             try:
#                 answer = optset(n, k)
#             except KeyError as e:
#                 print(n, k)
#                 print('KeyError', e)
#                 continue
#             if answer is True:
#                 continue
#             curr = 0
#             for num in answer:
#                 if num > n:
#                     print(n, k)
#                     print(answer)
#                     print(answer1)
#                     raise Exception('Number Exceeded')
#                 curr ^= num
            
#             if answer.__len__() != k:
#                 print(n, k)
#                 print(answer)
#                 print(len(answer))
#                 print(answer1, curr)
#                 raise Exception('Length not same')

#             if curr != answer1:
#                 print(n, k)
#                 print(answer)
#                 print(answer1, curr)
#                 raise Exception('XOR not same')
# something()