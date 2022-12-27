first = 1
second = 1
current = 0
sum = 0
while (current <= 4000000):
	current = first + second
	first = second
	second = current
	if (current % 2 == 0):
		sum += current
print(sum)
