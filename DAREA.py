from collections import defaultdict as dd

def darea(points):
    X = set()
    Y = set()
    x_dict = dd(lambda: [1e9 + 1, -1])
    y_dict = dd(lambda: [1e9 + 1, -1])
    for x, y in points:
    # for _ in range(int(input())):
    #     x, y = map(int, input().split())
        x_dict[x][1] = max(x_dict[x][1], y)
        x_dict[x][0] = min(x_dict[x][0], y)
        y_dict[y][1] = max(y_dict[y][1], x)
        y_dict[y][0] = min(y_dict[y][0], x)
        X.add(x)
        Y.add(y)

    
    if len(X) == 1 or len(Y) == 1:
        return 0
    
    sorted_x = sorted(X)
    sorted_y = sorted(Y)
    
    bt_min = [y_dict[sorted_y[0]][0]] * len(Y)
    bt_max = [y_dict[sorted_y[0]][1]] * len(Y)

    for index, y in enumerate(sorted_y[1 :], start=1):
        bt_min[index] = min(bt_min[index - 1], y_dict[y][0])
        bt_max[index] = max(bt_max[index - 1], y_dict[y][1])
    
    td_min = [y_dict[sorted_y[-1]][0]] * len(Y)
    td_max = [y_dict[sorted_y[-1]][1]] * len(Y)

    for index in range(len(Y) - 2, -1, -1):
        td_min[index] = min(td_min[index + 1], y_dict[sorted_y[index]][0])
        td_max[index] = max(td_max[index + 1], y_dict[sorted_y[index]][1])
    
    rl_min = [x_dict[sorted_x[0]][0]] * len(X)
    rl_max = [x_dict[sorted_x[0]][1]] * len(X)

    for index, x in enumerate(sorted_x[1 :], start=1):
        rl_min[index] = min(rl_min[index - 1], x_dict[x][0])
        rl_max[index] = max(rl_max[index - 1], x_dict[x][1])
    
    lr_min = [x_dict[sorted_x[-1]][0]] * len(X)
    lr_max = [x_dict[sorted_x[-1]][1]] * len(X)

    for index in range(len(X) - 2, -1, -1):
        lr_min[index] = min(lr_min[index + 1], x_dict[sorted_x[index]][0])
        lr_max[index] = max(lr_max[index + 1], x_dict[sorted_x[index]][1])
    
    
    answer = min((sorted_y[-1] - sorted_y[1]) * (td_max[1] - td_min[1]), (sorted_y[-2] - sorted_y[0]) * (bt_max[-2] - bt_min[-2]))
    for i in range(1, len(Y) - 1):
        print(
            answer,
            (sorted_y[i] - sorted_y[0]) * (bt_max[i] - min(bt_min[i - 1], td_max[i])) + (sorted_y[-1] - sorted_y[i]) * (max(td_max[i + 1], bt_min[i]) - td_min[i]),
            (sorted_y[i] - sorted_y[0]) * (max(bt_max[i - 1], td_min[i]) - bt_min[i]) + (sorted_y[-1] - sorted_y[i]) * (td_max[i] - min(td_min[i + 1], bt_max[i])),
        )
        answer = min(
            answer,
            (sorted_y[i] - sorted_y[0]) * (bt_max[i] - min(bt_min[i - 1], td_max[i])) + (sorted_y[-1] - sorted_y[i]) * (max(td_max[i + 1], bt_min[i]) - td_min[i]),
            (sorted_y[i] - sorted_y[0]) * (max(bt_max[i - 1], td_min[i]) - bt_min[i]) + (sorted_y[-1] - sorted_y[i]) * (td_max[i] - min(td_min[i + 1], bt_max[i])),
        )
        if i != len(Y) - 2:
            answer = min(answer, (sorted_y[i] - sorted_y[0]) * (bt_max[i] - bt_min[i]) + (sorted_y[-1] - sorted_y[i + 1]) * (td_max[i + 1] - td_min[i + 1]))
    

    answer = min(
        answer,
        (sorted_x[-1] - sorted_x[1]) * (lr_max[1] - lr_min[1]),
        (sorted_x[-2] - sorted_x[0]) * (rl_max[-2] - rl_min[-2])
    )

    for i in range(1, len(X) - 1):
        answer = min(
            answer, 
            (sorted_x[i] - sorted_x[0]) * (rl_max[i] - min(rl_min[i - 1], lr_max[i])) + (sorted_x[-1] - sorted_x[i]) * (max(lr_max[i + 1], rl_min[i]) - lr_min[i]),
            (sorted_x[i] - sorted_x[0]) * (max(rl_max[i - 1], lr_min[i]) - rl_min[i]) + (sorted_x[-1] - sorted_x[i]) * (lr_max[i] - min(lr_min[i + 1], rl_min[i])),
        )
        if i != len(X) - 2:
            answer = min(answer, (sorted_x[i] - sorted_x[0]) * (rl_max[i] - rl_min[i]) + (sorted_x[-1] - sorted_x[i + 1]) * (lr_max[i + 1] - lr_min[i + 1]))
    
    return answer


print(darea([[5, 1], [4, 2], [5, 2], [3, 2], [3, 4]]))
exit()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        print(darea())

