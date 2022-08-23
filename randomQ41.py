class TreeNode():
    def __init__(self, val):
        self.val = val
        self.children = []
        
def minSwap(numbers):
	
    n = len(numbers)
    answer = 0
    temp = numbers.copy()
    pos = {}
    temp.sort()

    for index, num in enumerate(numbers):
        pos[num] = index
		
    init = 0
	
    for i in range(n):

        if (numbers[i] != temp[i]):
            answer += 1
            init = numbers[i]

            numbers[i], numbers[pos[temp[i]]] = numbers[pos[temp[i]]], numbers[i]

            pos[init] = pos[temp[i]]
            pos[temp[i]] = i
			
    return answer


def swap_sort(n, A, edges):

    nodes = [TreeNode(val) for val in A]
    
    for a, b in edges:
        nodes[a - 1].children.append(nodes[b - 1])
    
    answer = 0
    
    depth = [nodes[0]]
    
    while len(depth):
        horizontal = []
        values = []
        for node in depth:
            for child in node.children:
                horizontal.append(child)
                values.append(child.val)
        
        answer += minSwap(values)
        depth = sorted(horizontal, key=lambda x: x.val)
    
    return answer

print(swap_sort(4, [1, 2, 3, 4], [(1, 3), (1, 2), (3, 4)]))
print(swap_sort(5, [10, 5, 6, 4, 7], [(1, 3), (1, 2), (3, 4), (2, 5)]))