a=open('input.txt','r')
c=a.read()
flag = 0
for i in range(len(c)):
    if c[i]=='@':
        flag =1
        break
a.close() 
if flag ==1:
    print('YES')
else:
    print('NO')