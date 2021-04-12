n = int(input())
w = list(map(int,input().split()))
w_count = sum(w)//2
w.sort()
w = w[::-1]
a = [[0]*(w_count+1) for i in range(n+1)]
for k in range(1,n+1):
    for s in range(1,w_count+1):
        if s >= w[k-1] :
            a[k][s] = max(a[k-1][s],a[k-1][s-w[k-1]]+w[k-1])
        else: a[k][s] = a[k-1][s]
ans = []
def f(k,s,ans):
    if a[k][s] == 0:return ans
    if a[k-1][s] == a[k][s]: return f(k-1,s,ans)
    else: ans.append(w[k-1]); return f(k-1,s-w[k-1],ans)
ans = f(k,s,ans)
print(sum(w)-2*sum(ans))