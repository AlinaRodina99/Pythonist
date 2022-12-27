def checkPalindrome(n):
	temp = n
	reverse_ = 0
	while (n > 0):
		digit = n % 10
		reverse_ = reverse_ * 10 + digit
		n = n // 10
	if (temp == reverse_):
		return True
	else:
		return False
def findLargestPalindrome():
	current = 0
	for i in range(100, 1000):
		for j in range(100, 1000):
			mult = i * j
			if checkPalindrome(mult):
				if mult > current:
					current = mult
	return current
