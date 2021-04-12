K = int(input())
h = 2 + (K % 5) + 7*(K // 5)
if K > 36:
    h+= 1
if K > 43:
    h+= 1
print(h)
