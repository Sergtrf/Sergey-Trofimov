k = int(input())
n = [0] * k
for i in range(len(n)):
    n[i] = int(input())
    
def BubbleSort(a):
    t = len(a) - 1
    while t > 0:
        bound = t
        t = 0
        i = 0
        while i < bound:
            if a[i+1] < a[i]:
                buf = a[i]
                a[i] = a[i+1]
                a[i+1] = buf
                t = i
            i += 1
    return a

print(BubbleSort(n))