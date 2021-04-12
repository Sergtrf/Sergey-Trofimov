def BinSearch(n, k):
    print('*')
    mid = len(n)//2
    if n[mid] > k:
        return BinSearch(n[:mid], k)
    elif n[mid] < k:
        return BinSearch(n[mid + 1:], k)
    else:
        return mid
    
k = int(input())
A = [0] * k
for i in range(len(A)):
    A[i] = int(input())
    
k = int(input())    
print(BinSearch(A, k))
        
