a= open('input.txt','r')
r = open('output.txt','w')
t=a.read().split()
q=0
w=0
for i in range(len(t)):
    if len(t[i])>q:
        q= len(t[i])
        w= t[i]
print(w, file = r)
a.close()
r.close()