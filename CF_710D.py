from collections import defaultdict as dd


def cf_710D(numbers: list):
    
    nums = dd(int)
    
    for num in numbers:
        nums[num] += 1
    
    counts = list(nums.values())
    if not n % 2 and len(set(numbers)) > 1:
        return 0
    prefixArr = [0]
    
    for num in counts:
        prefixArr.append(prefixArr[-1] + num)
        
    return min([abs(2 * i - n) for i in prefixArr])
    
            


if __name__ == '__main__':

    for _ in range(int(input())):
        n = int(input())
        print(cf_710D(list(map(int, input().split()))))