def sumSquaredFirstNNums(n):
	return n * (n + 1) * (2 * n + 1) / 6

def squareOfSumFirstNNums(n):
	return (n * (n + 1) / 2) ** 2

print(squareOfSumFirstNNums(100) - sumSquaredFirstNNums(100))

