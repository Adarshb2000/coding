def getBusinessNode(root):
    getSum(root)
    return answer

maxVal = -1
answer = 0

def getSum(root):
    global answer, maxVal
    if not root:
        return 
    if not len(root.children):
        return root.value, 1
    currSum = root.value
    count = 1
    for child in root.children:
        temp, c = getSum(child)
        count += c
        currSum += temp
            
    if currSum / count > maxVal:
        answer = root
        maxVal = currSum / count    
    return currSum, count
    
    
    
