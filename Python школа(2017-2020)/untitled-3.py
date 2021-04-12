a = open('input.txt', 'r', encoding = 'utf - 8')
a1 = open('output.txt', 'w')
c = a.readline()
w = 0
ww = 0
k = 0
k1 = 0
while len(c) != 0:
    n1, n2, c, b = c.split()
    b = int(b)
    if b == w:
        k1 += 1
    elif b > w and k1 == 0:
        w = b
        k1 = 1
    elif b > w and k1 > 0:
        ww = w
        w = b
        k = k1
        k1 = 1
    elif ww < b < w:
        ww = b
        k = 1
    elif b == ww:
        k += 1
    c = a.readline()
print(ww, k, file = a1)
a1.close()