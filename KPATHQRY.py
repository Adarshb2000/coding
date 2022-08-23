from collections import defaultdict as dd

def postOrder(root : int):
    global ends
    child_in_query = False
    num_o_true = 0
    for child in tree[root]:
        temp = postOrder(child)
        if temp:
            num_o_true += 1
        child_in_query = temp + child_in_query
        
    if num_o_true > 2:
        raise Exception
    
    elif num_o_true == 2:
        if N != child_in_query - 1:
            raise Exception
        else:
            raise FileNotFoundError

    if not child_in_query and root in query:
        ends += 1
    
    if ends > 2:
        raise Exception
    
    return int(root in query) + num_o_true


if __name__ == '__main__':
    
    for _ in range(int(input())):
        N = int(input())
        tree = dd(list)
        root = None
        for _ in range(N - 1):
            parent, child = map(int, input().split())
            if root is None:
                root = parent
            tree[parent].append(child)

        
        for _ in range(int(input())):
            ends = 0
            query = set(map(int, input().split()))
            try:
                postOrder(root)
                print('Yes')
            except FileNotFoundError:
                print('Yes')
            except Exception:
                print('No')