a = open('input.txt', 'r')
b = open('output.txt', 'w')
k = a.readlines()
a.close()
obr = k[0]
zam = k[1]
q = k.strip(".'''':'';''!")
for i in k[2].split(' '):
    if obr in i:
        print(k[2], file = b)
        b.close()
    else:
        if i == obr:
            i = zam
            print(k[2], file = b)
            b.close()