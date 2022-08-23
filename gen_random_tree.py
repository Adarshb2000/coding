from random import choice, randint

def genRandomTree(n: int):
    nodes = list(range(1, n + 1))
    available_nodes = set(nodes)
    available_nodes.discard(1)
    curr_start = 1
    curr_end = 1
    tree = []

    curr_child = 2

    while curr_child <= n:
        for root in range(curr_start, curr_end + 1):
            children = randint(1, n - curr_child + 1)
            for _ in range(children):
                tree.append([root, curr_child])
                curr_child += 1
            
            curr_start = curr_end + 1
            curr_end = curr_child - 1
    
    return tree


if __name__ == '__main__':
    n = 8
    while True:
        try:
            x = genRandomTree(n)
        except ValueError:
            continue
        break
    print(x)

