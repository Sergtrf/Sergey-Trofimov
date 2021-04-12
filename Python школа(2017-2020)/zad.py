k = int(input())
n = [0] * k
for i in range(len(n)):
    n[i] = int(input()) 

maxsum = n[0]
maxlen = 1
tsum = n[0]
tlen = 1
i = 1
while i < len(n):
    if n[i] <= n[i-1]:
        tsum += n[i]
        tlen += 1
    else:
        if maxsum < tsum:
            maxsum = tsum
            maxlen = tlen 
        elif maxsum == tsum:
            if maxlen < tlen:
                maxlen = tlen
        tsum = n[i]
        tlen = 1
    i += 1
if maxsum < tsum:
    maxsum = tsum
    maxlen = tlen
elif maxsum == tsum:
    if maxlen < tlen:
        maxlen = tlen
    
print(maxlen, maxsum)