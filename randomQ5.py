def cardinalitySort(nums):
    return [num for _, num in sorted([(bin(num).count('1'), num) for num in nums])]

if __name__ == '__main__':
    
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(int(input()))
    
    print(*cardinalitySort(nums), sep='\n')