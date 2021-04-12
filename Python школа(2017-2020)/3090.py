n, m = list(map(int, input().split()))
P = list(map(int, input().split())); c = list(map(int, input().split()))
A = [[0] * (m + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if j - P[i - 1] >= 0: A[i][j] = max(A[i - 1][j], A[i - 1][j - P[i - 1]] + c[i - 1])
        else: A[i][j] = A[i - 1][j]
x, y = n, m; l =[]
while A[x][y] != 0:
    if A[x][y] != A[x - 1][y]: y -= P[x - 1]; l.append(x)
    x -= 1
for i in l[::-1]: print(i)
