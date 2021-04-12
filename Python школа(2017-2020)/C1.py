f = open('input.txt','r') 
r = open('output.txt','w') 
a = list(map(int,f.read().split()))
n = 0 
s = 1 
c = [0] 
for i in range(len(a)):
    if a[n] == a[i] and n != i:
        s += 1
    else:
        c.append(s)
        s = 1
        n = i 
c.append(s) 
print(str(max(c)),file = r)