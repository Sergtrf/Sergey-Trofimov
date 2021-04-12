n = int(input())
buf1 = [int(input()) for i in range(4)]
buf2 = buf1[:3]
kpar = 0
kch1 = 0; knech1 = 0
kch2 = 0; knech2 = 0
if (buf1[3] + buf2[0])%2 == 1:
   kpar += 1
   kch2 += 1
   knech2 += 1
   buf2 = buf2[1:]; buf2.append(buf1[3])
for i in range(n - 4):
   a = int(input())
   b1 = buf1[0]; buf1 = buf1[1:]; buf1.append(a)
   b2 = buf2[0]; buf2 = buf2[1:]; buf2.append(a); print(buf2, buf1)
   k1 = int(a%2 == 0) + int(b1%2 == 0)
   k2 = int(a%2 == 0) + int(b2%2 == 0)  
   kch1 += k1; knech1 += (2 - k1)
   kch2 += k2; knech2 += (2 - k2)
   if a%2 == 0:
      kpar += kch1
   else:
      kpar += knech1
print(kpar)