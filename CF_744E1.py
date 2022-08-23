from collections import deque

def cf_744E(numbers):
    nums = deque()
    for num in numbers[1 :]:
        if len(nums) and num > nums[0]:
            nums.append(num)
        else:
            nums.appendleft(num)
    
    
    return list(nums)

if __name__ == '__main__':
    
    for _ in range(int(input())):
        input()
        print(*cf_744E(list(map(int, input().split()))))