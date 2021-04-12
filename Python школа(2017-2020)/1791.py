n = list(input());n2 = len(n)
m = list(input());m2 = len(m)    
a = [[0]*(m2+1) for i in range(n2+1)]
a[0] = [i for i in range(m2+1)]
for i in range(n2+1):
    a[i][0] = i

for i in range(1,n2+1):
    for j in range(1,m2+1):
        if n[i-1] == m[j-1]: a[i][j] = a[i-1][j-1]
        else: a[i][j] = min(a[i-1][j],a[i-1][j-1],a[i][j-1]) + 1
print(a[-1][-1])

#ABCDEFGH
#ACDEXGIH