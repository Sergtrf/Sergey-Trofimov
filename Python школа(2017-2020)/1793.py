a = [int(i) for i in input().split()]
n = len(a)
d = [None]*n
p = [None]*n
for i in range(n):
    d[i] = 1
    p[i] = -1
    for j in range(i):
        if a[j] < a[i]:
            if 1 + d[j] > d[i]:
                d[i] = 1 + d[j]
                p[i] = j
an = d[0]
for i in range(n):
    if d[i] > an:
        an = d[i]
        po = i
pa = []
while po != -1:
    pa.append(po)
    po = p[po]
print(len(pa))