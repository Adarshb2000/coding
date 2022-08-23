def createPalindrome(num):
    palindrome = num
    num //= 10
  
    while (num > 0):
        palindrome = palindrome * 10 + (num % 10)
        num //= 10

    return palindrome

def getAllChefora():
    answer = [0]
    i = 1
    a = -1 

    for i in range(1, MAX + 1):
        a = createPalindrome(i)
        answer.append(a)
        i += 1
    
    return answer


def getPrefixSum(numbers: list):
    answer = [0]
    for num in numbers[1 :]:
        answer.append(answer[-1] + num)

    
    return answer


def chefora(l: int, r: int):
    return pow(cheforas[l], prefix_sum[r] - prefix_sum[l], mod)
    


if __name__ == '__main__':
    
    MAX = 10 ** 5
    mod = 10 ** 9 + 7
    cheforas = getAllChefora()
    prefix_sum = getPrefixSum(cheforas)
    for _ in range(int(input())):
        print(chefora(*map(int, input().split())))
