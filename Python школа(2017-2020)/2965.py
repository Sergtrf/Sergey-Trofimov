n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
path = []
b = []
for i in range(n + 1): b.append(list(0 for i in range(m + 1)))
b[1][1] = a[0][0]
path = []
for i in range(n):
    for j in range(m):
        b[i + 1][j + 1] = a[i][j] + max(b[i][j + 1], b[i + 1][j])        
print(b[-1][-1])
ans = ''
i, j = n, m
while i > 0 and j > 0 :
    if i == 1 and j == 1: break
    if (b[i - 1][j] > b[i][j - 1] and i - 1 != 0 ) or (b[i][j - 1] == 0 and j - 1 == 0):
        ans = "D" + ans
        i -= 1
    else:
        ans = "R" + ans
        j -= 1
if ans != '': print(*ans)