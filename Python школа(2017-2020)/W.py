k = int(input())
n = [0] * k
for i in range(len(n)):
    n[i] = int(input())
    
def InsertSort(a):
    i = 1
    while (i < len(a)):
        buf = a[i]
        loc = i - 1
        while loc >= 0 and a[loc] > buf:
            a[loc+1] = a [loc]
            loc -= 1
        a[loc+1] = buf
        i += 1
    return a

print(InsertSort(n))


N, M, K = map(int, input().split())
'''