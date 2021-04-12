n = int(input())
a = n//10
b=b2 = n//5
c=c2 = n//2
d=d2 = n
summa = 0
while a != -1:
    p = n-a*10
    if p == 0:
        summa += 1
        a -= 1
    else:
        a -= 1
        while b != -1:
            p2 = p-b*5
            if p2 == 0:
                summa += 1
                b -= 1
            else:
                b -= 1
                if p2 > 0:
                    summa += 1+p2//2
        else:
            b = b2
print(summa)