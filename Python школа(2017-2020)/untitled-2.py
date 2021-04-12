a = open('input.txt', 'r')
c = a.readlines()
a.close()
def bukva(n):
    if ord ('A')<=ord(n)<=ord('Z'):
        return True
    elif ord('a')<=ord(n)<=ord('z'):
        return True
    else:
        return False
   
def CountWords(n):
    k = 0
    l = 0
    for i in range(0,len(n),1):
        if bukva (n[i]):
            l += 1
            if l == 1:
                k += 1
        else:
            l = 0
    return k

lines = 0
let = 0
w = 0
for i in range(len(c)):
    lines += 1
    
for i in range(len(c)):
    w += CountWords(c[i])
    for j in range(len(c[i])):
        if ord('a') <= ord(c[i][j]) <= ord('z') or ord('A') <= ord(c[i][j]) <= ord('Z'):
            let += 1

print('Input file contains:')
print(let, 'letters')
print(w, 'words')
print(lines, 'lines')