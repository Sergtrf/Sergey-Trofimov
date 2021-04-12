INF = float('inf')

n, s, f = map(int, input().split())
W = [list(map(int, input().split())) for i in range(n)]
#m, l = map(int, input().split())
for i in range(n):
    for j in range(n):
        if W[i][j] < 0:
            W[i][j] = INF

active = [True]*n
R = W[s - 1][:]     
P = [0]*n
active[s - 1] = False
P[s - 1] = -1
Q = []
Q.append(s)
kMin = s - 1
for i in range(n - 1):
    minDist = INF
    for j in range(n):
        if active[j] and R[j] < minDist:
            minDist = R[j]
            kMin = j
    Q.append(kMin + 1)
    active[kMin] = False
    for j in range(n):
        if R[kMin] + W[kMin][j] < R[j]:
            R[j] = R[kMin] + W[kMin][j]
            P[j] = kMin
if R[f - 1] == INF: print(-1)
else:
    print(*Q)
    
#else: print([f - 1])
