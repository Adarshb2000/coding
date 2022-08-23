from random import randint
from KAVGMAT import kavgmat
from KAVGMAT_cheating import method1 as test

def method0(n, m, matrix):
    sum_matrix = [[0 for _ in range(m)] for _ in range(n)]

    sum_matrix[0][0] = matrix[0][0]

    for i in range(1, m):
        sum_matrix[0][i] = sum_matrix[0][i - 1] + matrix[0][i]
    
    for i in range(1, n):
        sum_matrix[i][0] = sum_matrix[i - 1][0] + matrix[i][0]

    
    for i in range(1, n):
        for j in range(1, m):
            sum_matrix[i][j] = sum_matrix[i - 1][j] + sum_matrix[i][j - 1] + matrix[i][j] - sum_matrix[i - 1][j - 1]

    
    # for i in range(n):
    #     print(*sum_matrix[i]);

    

    answer = 0
    sum_ = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] > -1:
                answer += 1

    for size in range(1, n):
        for i in range(n - size):
            for j in range(m - size):
                if i > 0 or j > 0:
                    if i > 0 and j > 0:
                        sum_ = sum_matrix[i + size][j + size] - sum_matrix[i - 1][j + size] - sum_matrix[i + size][j  - 1] + sum_matrix[i - 1][j - 1]
                    elif i > 0:
                        sum_ = sum_matrix[i + size][j + size] - sum_matrix[i - 1][j + size]
                    elif j > 0:
                        sum_ = sum_matrix[i + size][j + size] - sum_matrix[i + size][j - 1]
                else:
                    sum_ = sum_matrix[i + size][j + size]
                    
                if sum_ > -1:
                    answer += 1

    return answer




# Python3 programm to count total number
# of k x k sub matrix whose sum is
# greater than the given number S

dim = 3

# Function to create prefix sum
# matrix from the given matrix
def createTable(mtrx, k, p, dp):
	
	# Store first value in table
	dp[0][0] = mtrx[0][0]
	
	# Initialize first row of matrix
	for j in range(1, dim):
		dp[0][j] = mtrx[0][j] + dp[0][j - 1]
	
	# Initialize first coloumn of matrix
	for i in range(1, dim):
		dp[i][0] = mtrx[i][0] + dp[i - 1][0]
	
	# Initialize rest table with sum
	for i in range(1, dim):
		for j in range(1, dim):
			dp[i][j] = (mtrx[i][j] +
						dp[i - 1][j] +
						dp[i][j - 1] -
						dp[i - 1][j - 1])
		
# Utility function to count the submatrix
# whose sum is greater than the S
def countSubMatrixUtil(dp, k, p):
	
	count = 0
	subMatSum = 0
	
	# Loop to iterate over all the
	# possible positions of the
	# given matrix mat[][]
	for i in range(k - 1, dim):
		for j in range(k - 1, dim, 1):
			if (i == (k - 1) or j == (k - 1)):
				
				# Condition to check, if K x K
				# is first sub matrix
				if (i == (k - 1) and j == (k - 1)):
					subMatSum = dp[i][j]
					
				# Condition to check sub-matrix
				# has no margin at top
				elif (i == (k - 1)):
					subMatSum = dp[i][j] - dp[i][j - k]
					
				# Condition when sub matrix
				# has no margin at left
				else:
					subMatSum = dp[i][j] - dp[i - k][j]
					
			# Condtion when submatrix has
			# margin at top and left
			else:
				subMatSum = (dp[i][j] -
							dp[i - k][j] -
							dp[i][j - k] +
							dp[i - k][j - k])
			
			# Increament count, If sub matrix
			# sum is greater than S
			if (subMatSum >= p):
				count += 1
				
	return count
	
# Function to count submatrix of
# size k x k such that sum if
# greater than or equal to S
def countSubMatrix(mtrx, k, p):
	
	dp = [[0 for i in range(dim)]
			for j in range(dim)]
	
	# For loop to initialize prefix sum
	# matrix with zero, initially
	for i in range(dim):
		for j in range(dim):
			dp[i][j] = 0
	
	# Function to create the
	# prefix sum matrix
	createTable(mtrx, k, p, dp)
	
	return countSubMatrixUtil(dp, k, p)


if __name__ == '__main__':
    n = m = dim
    matrix = [[randint(-5, 5) for _ in range(m)] for _ in range(n)]

    # matrix = [[matrix[i][j]for j in range(m)] for i in range(n)]

    answer0 = test(n, m, matrix)
    answer1 = 0
    for k in range(1, n + 1):
        answer1 += countSubMatrix(matrix, k, 0)

    if answer0 != answer1:
        print(answer0, answer1, sep='\n')
        for i in range(n):
            for j in range(m):
                if matrix[i][j] > -1:
                    print('0', end='')
                print(matrix[i][j], end=' ')
            print()
        
        print('\n')
        print(matrix)
    