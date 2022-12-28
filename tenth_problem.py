def eratosthenes(n):
	multiples = set()
	for i in range(2, n + 1):
		if i not in multiples:
			yield i
			multiples.update(range(i * i, n + 1, i))
sum = 0
ml = list(eratosthenes(2000000))
for x in ml:
	sum += int(x)
print(sum)
