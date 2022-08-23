def maximumPoints(k, costs):
    last = 0
    for i, cost in enumerate(costs):
        k -= cost
        if k < 0:
            last = i
            break
    else:
        return len(cost)

    k += max(costs[: last + 1])

    answer = last
    last += 1
    while k > 0:
        k -= costs[last]
        last += 1
        if last == len(costs):
            return len(costs) - 1
    

    return max(answer, last - 1)

print(maximumPoints(10, [5, 2, 3, 4, 1]))
    