n,w = list(map(int, input().split())); P = list(map(int, input().split()))
A = [[0] * (w + 1) for i in range(n + 1)]; s = sum(P)
if s < w: print('NO')
else:
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if j - P[i - 1] >= 0:
                A[i][j] = max(A[i - 1][j], A[i - 1][j - P[i - 1]] + P[i - 1])
            else:
                A[i][j] = A[i - 1][j]
    if A[-1][-1] != w:
        print('NO')
    else:
        print('YES')
