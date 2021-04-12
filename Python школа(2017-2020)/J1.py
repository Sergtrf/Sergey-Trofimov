n, k = map(int, input().split())
a = []
b = max(n, k)
c = min(n, k)
for i in range(2):
        a.append([])
        for j in range(b):
                a[i].append(1)
for i in range(c):
        for j in range(b):
                if j + 1 < b:
                        a[1][j + 1] = a[1][j] + a[0][j + 1]
        a[0], a[1] = a[1], a[0]
print(a[-1][-1] % 1000007)