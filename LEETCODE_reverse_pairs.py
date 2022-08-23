def revesePairs(numbers: list):
    def divide(numbers: list):
        n = len(numbers)
        if n == 1:
            return numbers
        else:
            array = merge(divide(numbers[: n // 2]), divide(numbers[n // 2 :]))
            return array

    def merge(numbers1: list, numbers2: list):
        n = len(numbers1)
        m = len(numbers2)
        i = 0
        j = 0
        numbers = []
        while i < n and j < m:
            if numbers1[i] > numbers2[j]:
                numbers.append(numbers2[j])
                j += 1
            else:
                numbers.append(numbers1[i])
                i += 1
            
        while i < n:
            numbers.append(numbers1[i])
            i += 1
        
        while j < m:
            numbers.append(numbers2[j])
            j += 1
        
        while numbers1 and numbers2:
            while len(numbers1) and len(numbers2) and numbers1[-1] > 2 * numbers2[-1]:
                answer += len(numbers2)
                numbers1.pop()

            while len(numbers1) and len(numbers2) and numbers1[-1] <= 2 * numbers2[-1]:
                numbers2.pop()
            
        
        
        
        return numbers
    
    divide(numbers)
    return answer
answer = 0
print(revesePairs([1,3,2,3,1]))