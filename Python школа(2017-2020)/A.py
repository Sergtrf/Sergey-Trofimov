n = int(input())
k = 1
l = 1
u = 0
q = 1
while n >= u:
    q += 1
    if n == u:
        print(q)
        break
    elif n == 1:
        print(2)
        break
    u = k + l
    l = k
    k = u
    if n < u:
        print(-1)