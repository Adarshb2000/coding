def recur(i: int, oddSet: set, lenght: int, string: str):
    global dp, MOD
    if i == len(string):
        return (lenght % 2 and len(oddSet) == 1) or (lenght % 2 == len(oddSet) == 0)
    
    if (i, tuple(oddSet)) in dp:
        return dp[(i, tuple(oddSet))]
    
    # Inclusive
    temp = oddSet.copy()
    if string[i] in temp:
        temp.discard(string[i])
    else:
        temp.add(string[i])

    inc = recur(i + 1, temp, lenght + 1, string)
    
    
    # Exclusive
    exc = recur(i + 1, oddSet.copy(), lenght, string)
    
    dp[(i, tuple(oddSet))] = (inc + exc) % MOD
    return dp[(i, tuple(oddSet))]

def func(string: str):
    global dp, MOD
    dp = {}
    MOD = 10 ** 9 + 7
    return recur(0, set(), 0, string)



from string import ascii_lowercase
from random import choice, randint
while True:    
    string = ''
    for i in range(randint(1, 100)):
        string += choice(ascii_lowercase)
    answer1 = func(string)