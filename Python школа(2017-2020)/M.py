a = open('input.txt', 'r')
b = open('output.txt', 'w')
k = a.readlines()
k = [i.strip().split() for i in k]
a.close()
q = []
for i in k:
    for j in i:
        if ('a' in j[0]) or ('A' in j[0]):
            q.append(i)
            break
if len(q) != 0:
    for i in q:
        print(*i, file = b)
else:
    print(0, file = b)
b.close()