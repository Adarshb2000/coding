def evenSubarray(numbers, k):
    odd_count = [0]
    for num in numbers:
        odd_count.append(odd_count[-1] + int(num & 1))
    
    odd_count_dict = {}
    for index, count in enumerate(odd_count):
        if count not in odd_count_dict:
            odd_count_dict[count] = index - 1
    
    answers = set()
    
    for i, num in enumerate(numbers):
        curr = odd_count[i + 1] 
        if not num & 1:
            curr += 1
        end = odd_count_dict.get(curr + k, len(numbers))
        for j in range(i, end + 1):
            answers.add(tuple(numbers[i : j]))
    
    print(answers)
    
    return len(answers)
            

if __name__ == '__main__':
    
    n = int(input())
    numbers = []
    for _ in range(n):
        numbers.append(int(input()))
        
    k = int(input())
    print(evenSubarray(numbers, k))