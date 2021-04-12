a = input()
b = input()
q = ''
o = 0
n = 1
for i in range(len(b)):
    if b[i].isdigit() == True:
        break
    elif b[i] == '*':
        b[i:]
if len(a) > len(b):
    b += '0'*(len(a) - len(b))
for i in range(len(a)):
    if b[i] != a[i] and b[i] != '?' and b[i] != '*':
        print('NO')
        break
    if b[i] != a[i] and b[i] == '?':
        b[i] = a[i]
    elif b[i] == '*':
        for j in range(len(a)):
            while n != 0:
                if b[i + 1] != a[j]:
                    q += a[j]
                else:
                    b = b[:i] + q + b[i + 1:]
                    print(b)
                    n = 0
    else: print('YES')
        