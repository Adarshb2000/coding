class Node:
    def __init__(self, val: int, left, right):
        self.val = val
        self.left = left
        self.right = right

def buildTree(root, val, string):
    node = root
    
    for i in range(len(string) - 1):
        if string[i] == 'L':
            node = node.left
        else:
            node = node.right
    
    child = Node(val)
    if string[-1] == 'L':
        node.left = child
    else:
        node.right = child
        
answer = 0

def checkMagicParent(root: Node):
    global answer
    if not root:
        return
    if not root.left or not root.right:
        return
    
    l, r = root.left.val, root.right.val
    
    if not l % r:
        answer += root.val
        return
    if not r % l:
        answer += root.val
        return

def fun(n, Root, pos, val):
    global answer
    root = Node(Root)
    treeNode = [(p, v) for p, v in zip(pos, val)]
    treeNode.sort()
    for p, v in treeNode:
        buildTree(root, v, p)
    answer = 0
    recur(root)

    return answer
    

def recur(root):
    if not root:
        return
    checkMagicParent(root)
    recur(root.left)
    recur(root.right)
    

    
    