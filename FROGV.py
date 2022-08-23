if __name__ == '__main__':
    
    n, k, p = list(map(int, input().split()))
    locations = list(map(int, input().split()))
    locations_dict = {}
    for i, location in enumerate(locations):
        locations_dict[location] = locations_dict.get(location, []) + [i]
    
    groups = [0] * n
    group = 0
    
    uniques = list(sorted(list(locations_dict.keys())))
    

    i = 0
    while i < len(uniques):
        for frog in locations_dict[uniques[i]]:
            groups[frog] = group
        if i == n - 1:
            break
        while uniques[i + 1] - uniques[i] < k + 1:
            for frog in locations_dict[uniques[i + 1]]:
                groups[frog] = group
            i += 1
            if i == n - 1:
                break
        group += 1
        i += 1
    
    
    for _ in range(p):
        a, b = list(map(int, input().split()))
        print("YES" if groups[a - 1] == groups[b - 1] else "NO")