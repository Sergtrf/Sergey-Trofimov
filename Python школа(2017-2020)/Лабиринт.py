def Print(a):
    for i in range (m+2):
        for j in range(n+2):
            print("%4d" % a[i][j],end='')
        print('\n',end='')
def Hod(a,i,j,d):
    a[i][j]=d
    if i == i2 and j==j2:
        Print(a)
        return
    else:
        for k in range(4):
            if a[i+dx[k]][j+dy[k]]==0:
                Hod (a,i+dx[k],j+dy[k],d+1)
        a[i][j]=0
m=7;n=5
print('<ЛАБИРИНТ>')
dx=[-1,0,0,1];dy=[0,-1,1,0]
a=[[0]*(n+2) for i in range(m+2)]
f=open('lab.txt','r')
for i in range(m+2):
    a[i]=list(map(int,f.readline().split()))
Print(a)    
f.close()
print('введите координаты входа:',end='')
i1,j1 = map(int,input().split())
print('введите кординатывыхода:',end='')
i2,j2 = map(int,input().split())
Hod(a,i1,j1,1);
if a[i2][j2]==0:print('проход невозможен')