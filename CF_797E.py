def CF797E(numbers, k):
    answer = 0
    nums = []
    for num in numbers:
        answer += num // k
        nums.append(num % k)

    counts = {}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    if k == 2:
        return answer if 1 not in counts else answer + counts[1] // 2
    
    temp = max(counts.keys())
    start = k - temp
    for i in range(temp, 1, -1):
        if i not in counts:
            continue

        start = max(start, k - i)
        while counts[i]:
            for j in range(start, k):
                if j not in counts or not counts[j]:
                    continue

                if i == j and counts[i] == 1:
                    continue

                start = j
                counts[j] -= 1
                counts[i] -= 1
                answer += 1
                break
            else:
                break
        else:
            continue
        break

    return answer




for _ in range(int(input())):
    _, k = map(int, input().split())
    print(CF797E(list(map(int, input().split())), k))