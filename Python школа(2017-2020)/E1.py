n, k = map(int, input().split())
l = int(input())
a = list(map(int, input().split()))
d = [0] * (k - 1) + [1]
print(d)
q = 1
for i in range(n - 2):
    if i in a:
        
    else:
        d.append(q)
        d1 = d[0]
        d = d[1:]
        q = 2 * d[-1] - d1
print(q)