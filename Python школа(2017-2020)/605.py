n = int(input())
a = [list(map(int,input().split())) for i in range(n)]
k = int(input())
c = [i for i in range(1,n+1)]
for i in range(k):
    x,y = map(int,input().split())
    r = c[min(x,y)-1]
    r2 = c[max(x,y)-1]
    for j in range(n):
        if c[j] == r2:
            c[j] = r
ans = 0
for i in range(len(set(c))-1):
    l = 1000000000
    for j in range(n):
        if c[j] == c[0]:
            for g in range(n):
                if c[g] != c[0]:
                    p = ((a[j][0]-a[g][0])**2+(a[j][1]-a[g][1])**2)**(1/2)
                    if l > p :
                        h = c[g]
                        l = p
    ans += l
    for j in range(n):
        if c[j] == h:
            c[j] = c[0]
print("%.5f" %ans)