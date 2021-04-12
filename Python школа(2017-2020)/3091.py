n,w = map(int, input().split()); P = sorted(list(map(int, input().split())), key = int, reverse = True)
A = [[0] * (w + 1) for i in range(n + 1)]; s = sum(P)
if s < w: print(0)
else:
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if j - P[i - 1] >= 0:
                A[i][j] = max(A[i - 1][j], A[i - 1][j - P[i - 1]] + P[i - 1])
            else:
                A[i][j] = A[i - 1][j]
    if A[-1][-1] != w:
        print(0)
    else:
        x, y = n, w
        p = 0
        while A[x][y] != 0:
            if A[x][y] != A[x - 1][y]:
                y -= P[x - 1]; p += 1
            x -= 1
        print(p)