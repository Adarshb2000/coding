def mmass(string):
    n = len(string)

    mass = {
        'C' : 12,
        'H' : 1,
        'O' : 16
    }

    brackets = 0
    multipliers = [0, 0]

    i = 0
    while i < n:
        if string[i] == '(':
            multipliers.append(0)
            brackets += 1
        elif string[i] == ')':
            brackets -= 1
            if i < n - 1:
                if string[i + 1].isnumeric():
                    i += 1
                    number = string[i]
                    i += 1
                    if i < n - 1:
                        while string[i].isnumeric():
                            number += string[i]
                            i += 1
                            if i == n:
                                break

                    number = int(number)

                    total = multipliers.pop() * number
                    multipliers[-1] += total
                    
                    i -= 1
            
            total = multipliers.pop()
            multipliers[-1] += total

        elif string[i].isalpha():
            element = mass[string[i]]

            if string[i + 1].isnumeric():
                number = ''
                i += 1
                if i < n - 1:
                    while string[i].isnumeric():
                        number += string[i]
                        i += 1
                        if i == n:
                            break

                number = int(number)
            
            else:
                number = 1

            multipliers[-1] += element * number
            
            i -= 1


        i += 1

    return sum(multipliers)            


if __name__ == '__main__':
    while True:
        try:
            print(mmass(input()))
        except EOFError