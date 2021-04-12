n = int(input())
u = 0
s = 0
for i in range(2**n):
    for j in bin(i)[2:]:
        if j == '1':
            s += 1
    if s < 3:
        u += 1
    s = 0
print(u)

n = int(input())
a = {1:0, 5:0, 6:0}
o = []
o.append(((n // 6), (n % 6)))
o.append(((n // 5), (n % 5)))
if sum(o[0]) < sum(o[1]):
    o.pop(1)
    print(sum(o[0]))
    a[1] += o[0][1]
    a[6] += o[0][0]
    print(*['6' for x in range(a[6])], *['1' for i in range(a[1])])
else:
    o.pop(0)
    print(sum(o[0]))
    a[1] += o[0][1]
    a[5] += o[0][0]    
    print(*['5' for y in range(a[5])], *['1' for i in range(a[1])])