def Int(k):
    l = 0
    for i in range(len(k)):
        l += (ord(k[i]) - ord('0')) * (10 ** (len(k) - i - 1))
    k = l
    return k
        
n = input()
n = Int(n)
u = ''
t = 0

while n > 0:
    u += chr(n % 2 + ord('0'))
    n = n//2

print(u[::-1])