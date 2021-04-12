n = int(input())
b = {}
for i in range(n):
    f, inic, num = input().split(' ')
    b[num[7:]] = b.get(num[7:], 0) + 1
print(n/len(b))