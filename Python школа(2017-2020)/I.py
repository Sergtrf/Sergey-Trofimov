a = open('input.txt', 'r')
b = open('output.txt', 'w')
k = a.readlines()
a.close()
o = []
l = int(k[0])
k.pop(0)
m = 1
for i in k:
        x, y, z = i.split(' ')
        q = y[0] + '.' + ' ' + x
        if int(z) > l:
                o.append(q)
for i in o:
        i.split()
print(len(o), file = b)
for i in o:
        d = str(m) + ') ' + i
        print(d, file = b)
        m += 1
b.close()