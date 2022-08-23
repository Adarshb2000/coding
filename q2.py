from random import randint, randrange

def something(numbers1, numbers2, k):
    from collections import defaultdict as dd
    def lowerBound(arr, low, high, el):
        if low == high:
            return arr[low]
        
        mid = (low + high) // 2 + 1
        
        if arr[mid] == el:
            return el
        elif arr[mid] < el:
            return lowerBound(arr, mid, high, el)
        else:
            return lowerBound(arr, low, mid - 1, el)
    
    numbers1_dict = dd(list)
    numbers2_dict = dd(list)
    ans = []
    optimal = 0
    for id_, req in numbers1:
        numbers1_dict[req].append(id_)
        
    for id_, req in numbers2:
        numbers2_dict[req].append(id_)
    
    nums1 = list(numbers1_dict.keys())
    nums2 = sorted(list(numbers2_dict.keys()))

    for i in nums1:
        req = k - i
        b = lowerBound(nums2, 0, nums2.__len__() - 1, req)

        if b + i <= k:
            if b + i < optimal: continue
            if b + i > optimal:
                ans = []
                optimal = b + i
            
            for id1_ in numbers1_dict[i]:
                for id2_ in numbers2_dict[b]:
                    ans.append([id1_, id2_])
    
    return ans

# print(something([[1, 4], [2, 6]], [[1, 2], [2, 9], [3, 5]], 19))
# exit()

def method2(numbers1, numbers2, k):
    ans = []
    optimal = 0
    for id1, i in numbers1:
        for id2, j in numbers2:
            if i + j <= k:
                if i + j > optimal:
                    ans = [[id1, id2]]
                    optimal = i + j
                elif i + j == optimal:
                    ans.append([id1, id2])

    return ans


if __name__ == '__main__':
    
    while True:
        n = randint(1, 5)
        m = randint(1, 5)
        numbers1 = [[i, randint(1, 10)] for i in range(1, n + 1)]
        numbers2 = [[i, randint(1, 10)] for i in range(1, m + 1)]
        k = randint(1, 25)
        answer0 = sorted(something(numbers1, numbers2, k))
        answer1 = sorted(method2(numbers1, numbers2, k))
        if answer0 != answer1:
            print(answer0, answer1, k)
            print(numbers1)
            print(numbers2)
            break
