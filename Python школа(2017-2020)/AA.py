n = int(input())
b = []
a = {}
q = 0
for i in range(10**(n//2)):
        b.append(i)
for i in b:
        for j in str(i):
                q += int(j)
        if q in a:
                a[q] += 1
        else:
                a[q] = 1
        q = 0
for i in a:
        if a[i] >= 2:
                for j in range(a[i]):
                        q += j
print(q * 2 + 10**(n//2))
