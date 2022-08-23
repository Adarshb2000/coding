def colglf4(inp):
    N, eggs, chocolates, omlet_price, milk_price, cake_price = inp
    
    if eggs > chocolates and N > chocolates + (eggs - chocolates) // 2:
        return -1
    elif chocolates > eggs and N > eggs + (chocolates - eggs) // 3:
        return -1
    elif chocolates == eggs and N > eggs:
        return -1
    
    x = min([omlet_price, milk_price, cake_price]) 

    if x == cake_price:
        if eggs >= N and chocolates >= N:
            return N * cake_price
        else:
            temp = min(eggs, chocolates)
            N -= temp
            eggs -= temp
            chocolates -= temp
            remaining  = milk_price if chocolates else omlet_price
                
            return temp * cake_price + N * remaining
    
    elif x == omlet_price:
        if eggs >= 2 * N:
            return N * omlet_price
        elif cake_price > milk_price:
            omelet = eggs // 2
            N -= omelet
            eggs -= 2 * omelet
            cake = 0
            if N <= chocolates // 3:
                return omelet * omlet_price + N * milk_price
            milk = chocolates // 3
            chocolates -= 3 * milk
            N -= milk
            if eggs:
                if chocolates == 1:
                    cake += 1
                elif chocolates == 2:
                    if N == 1:
                        return omelet * omlet_price + milk * milk_price + N * cake_price
                        
                    omelet -= 2
                    milk -= 1
                    cake += 5
                    N += 3

                else:
                    omelet -= 1
                    milk -= 1
                    cake += 3
                    N += 2
            else:
                if chocolates == 1:
                    cake += 4
                    omelet -= 2
                    milk -= 1
                    N += 3
                    
                elif chocolates == 2:
                    omelet -= 1
                    cake += 2
                    N += 1
            
            if N <= cake:
                return omelet * omlet_price + milk * milk_price + N * cake_price
            else:
                N -= cake
                omelet -= 3 * N
                milk -= 2 * N
                cake += 6 * N
                return omelet * omlet_price + milk * milk_price + cake * cake_price
        
        else:
            min_price = -1
            for i in range(eggs // 2 + 1):
                cake = eggs - 2 * i
                if i + cake >= N:
                    if chocolates < N - i:
                        continue
                    price = i * omlet_price + (N - i) * cake_price
                    if price < min_price or min_price == -1:
                        min_price = price
                else:
                    if chocolates < cake + (N - i - cake) * 3:
                        continue
                    price = i * omlet_price + cake * cake_price + (N - i - cake) * milk_price
                    if price < min_price or min_price == -1:
                        min_price = price

            return min_price
    
    else:
        if chocolates >= 3 * N:
            return N * milk_price
        elif cake_price > omlet_price:
            milk = chocolates // 3
            chocolates -= 3 * milk
            N -= milk
            omelet = eggs // 2
            eggs -= 2 * omelet
            if N <= omelet:
                return milk * milk_price + N * omlet_price
            N -= omelet
            cake = 0
            if eggs:
                if chocolates == 1:
                    cake += 1
                elif chocolates == 2:
                    if N == 1:
                        return omelet * omlet_price + milk * milk_price + N * cake_price
                    omelet -= 2
                    milk -= 1
                    cake += 5
                    N += 3
                else:
                    omelet -= 1
                    milk -= 1
                    cake += 3
                    N += 2
            else:
                if chocolates == 1:
                    cake += 4
                    omelet -= 2
                    milk -= 1
                    N += 3
                    
                elif chocolates == 2:
                    omelet -= 1
                    cake += 2
                    N += 1
            
            if N <= cake:
                return omelet * omlet_price + milk * milk_price + N * cake_price
            else:
                N -= cake
                omelet -= 3 * N
                milk -= 2 * N
                cake += 6 * N
                return omelet * omlet_price + milk * milk_price + cake * cake_price
        else:
            min_price = -1
            for i in range(chocolates // 3 + 1):
                cake = chocolates - 3 * i
                if i + cake >= N:
                    if eggs < N - i:
                        continue
                    price = i * milk_price + (N - i) * cake_price
                    if price < min_price or min_price == -1:
                        min_price = price
                else:
                    if eggs < cake + (N - i - cake) * 2: continue
                    price = i * milk_price + cake * cake_price + (N - i - cake) * omlet_price
                    if price < min_price or min_price == -1:
                        min_price = price

            return min_price
    
    

if __name__ == '__main__':
    t = int(input())

    while t:

        print(colglf4(list(map(int, input().split()))))

        t -= 1