n = int(input())
b = {}
for i in range(n):
    l = ''
    for j in input():
        if ord('0') <= ord(j) <= ord('9'):
            l += j
    b[l] = b.get(l, 0) + 1
b[l] = b.get(l, 0) + 1
l = 0
n = 1
while n <= len(b):
    n += 1
    for i in b:
        if b.get(i) > 5:
            l = i
    try:
        del b[l]
        n -= 1
    except KeyError:
        pass
print(len(b))
for i in b:
    print(i)