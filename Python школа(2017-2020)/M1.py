n, m = map(int, input().split())
a = []
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
q = a[0][0]
p = ''
i = 0
j = 0
while i < n and j < m:
    if a[i][j - 1] >= a[i - 1][j]:
        p += 'N'
        q += a[i][j - 1]
        i += 1
    else:
        p += 'E'
        q += a[i - 1][j]
        j += 1
if (n - i) == 1:
    p += 'N'
    q += a[n - 1][m - 1]
if (m - j) == 1:
    p += 'E'
    q += a[n - 1][m - 1]
print(q)
print(p)