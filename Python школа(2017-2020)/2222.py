def Print(A):
    for i in range(2,m+2):
        for j in range(2,n+2):
            print("%5d" %A[i][j],end=' ')
        print()
def Rec(i,j,t,a):
    global q
    if a[i][j]!=0:
        return
    else:
        a[i][j]=t
        if t==m*n:
            Print(a)
            q=True
            return
        else:
            for k in range(8):
                Rec(i+di[k], j+dj[k], t+1,a)
            a[i][j]=0
m=5
n=4
di=[-2,-1,1,2,2,1,-1,-2]
dj=[1,2,2,1,-1,-2,-2,-1]
A=[[0]*(n+4) for j in range(m+4)]
for i in range(m+4):
    for j in range(n+4):
        if i<2 or i>m+1 or j<2 or j>n+1:
            A[i][j]=-1

   
q=False
Rec(2,2,1,A)