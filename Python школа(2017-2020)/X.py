def Div(n):
    k, d, c, h = [0] * 4
    for i in range(len(n)):
        if i % 2 != 0:
            k += n[i]
            h += 1
        elif i % 2 == 0:
            d += n[i]
            c += 1
    return k/h, d/c

k = int(input())
A = [0] * k
for i in range(len(A)):
    A[i] = int(input())
    
print(Div(A))