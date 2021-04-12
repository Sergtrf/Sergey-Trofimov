def fmax(n):
    nmax = n[0]
    k = 0
    for i in range(len(n)):
        if n[i] > nmax:
            nmax = n[i]
            k = i
    return k

def fmin(n):
    nmin = n[0]
    k = 0
    for i in range(len(n)):
        if n[i] < nmin:
            nmin = n[i]
            k = i
    return k 

def change(n,i,j):
    n[i], n[j] = n[j], n[i]
    return n

k = int(input())
A = [0] * k
for i in range(len(A)):
    A[i] = int(input())
    
print (A)

c = fmax(A)
d = fmin(A)
print (c, d, change(A, d, c))


k = int(input())
A = []
for i in range(k):
    A.append (int(input()))

