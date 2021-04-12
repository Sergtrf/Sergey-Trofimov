def f(n):
	l = [5000, 1000, 500, 100, 50, 10, 5, 2, 1]
	d = {}
	
	for i in l:
		count = 0
		while n >= i:
			count += 1
			n -= i
		d[i] = count
	return d


def main(k):
	if K%2 != 0:
		return "NO"
	else:
		for i in f(K).values():
			if i%2 != 0:
				return "NO"
		return "YES"


K = int(input())
print(main(K))
