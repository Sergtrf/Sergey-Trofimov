n = int(input())
ans = []
for i in range(n):
    ans.append([])
for i in range(n):
    a = list(map(int,input().split()))
    ans[i].append(i)
    for j in range(n):
        if a[j] == 1:ans[i].append(j);ans[j].append(i)
summa = 0
for i in range(n):
    c = []
    for j in range(len(ans[i])):
        if ans[i][j] not in c : c.append(ans[i][j])
    if len(c) < 3: ans[i] = []
    else: summa += len(ans[i])-1
print(summa)
for i in range(n):
    if ans[i] == []:print(0,end = " ")
    else: print(len(ans[i])-1,end = " ")