def cf_713B(n: int):
    matrix = []
    first_index = False
    star_index = False
    for i in range(n):
        a = list(input())
        star_count = a.count('*')
        
        if star_count == 2:
            matrix.append(a.copy())
            if i == n - 1:
                matrix = matrix[1 :]

        elif star_count:
            if first_index is False:
                first_index = i
                star_index = a.index('*')
            else:
                temp = a.index('*')
                if temp == star_index:
                    x = -1 if temp == n - 1 else 1
                    matrix[first_index][temp + x] = '*'
                    a[temp + x] = '*'

                else:
                    matrix[first_index][temp] = '*'
                    a[star_index] = '*'
        
        matrix.append(a.copy())
    
    for i in range(n):
        print(*matrix[i], sep='')



if __name__ == '__main__':
    
    for _ in range(int(input())):
        cf_713B(int(input()))