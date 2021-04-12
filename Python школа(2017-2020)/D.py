import sys
N, M = [int(i) for i in input().split()]
 
i = 1
couple = []
while i <= N:
	j = 1
	while j <= M:
		couple.append((i, j))
		j += 1
	i += 1

d = {}

for i in range(0, len(couple), 2):
	print(couple[i][0], couple[i][1], couple[i+1][0], couple[i+1][1])
	sys.stdout.flush()
	a, b = [int(j) for j in input().split()]
	# dict.get(key[, default]) - возвращает значение ключа,
	# но если его нет, не бросает исключение, а возвращает default (по умолчанию None).
	if a != b:
		d_a = d.get(a, [])
		d_a.append(couple[i])
		d[a] = d_a
	   
		d_b = d.get(b, [])
		d_b.append(couple[i+1])
		d[b] = d_b
	   
		for k, v in d.items():
			if len(v) == 2:
				d[k] = []
				print(v[0][0], v[0][1], v[1][0], v[1][1])
				sys.stdout.flush()
				a, b = [int(j) for j in input().split()]
