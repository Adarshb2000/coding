from collections import defaultdict

def cf_748E(tree: defaultdict, k: int):
    for _ in range(k):
        if len(tree) in [1, 2]:
            return 0
        removed = defaultdict(list)
        for key, value in tree.items():
            if len(value) == 1:
                removed[value.pop()].append(key)
                
        
        for key, value in removed.items():
            for val in value:
                tree[key].discard(val)
                del tree[val]
    
    return len(tree)

                


if __name__ == '__main__':
    
    for _ in range(int(input())):
        input()
        n, k = map(int, input().split())
        tree = defaultdict(set)
        for _ in range(n - 1):
            x, y = map(int, input().split())
            tree[x].add(y)
            tree[y].add(x)
            
        print(cf_748E(tree, k))