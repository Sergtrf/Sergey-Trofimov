n = int(input())
if n == 1 or n == 2:
    print(1)
elif n == 3:
    print(2)
else:
    s3 = 1
    s2 = 2    
    for i in range(n - 3):        
        s1 = s2 +s3
        s3 = s2
        s2 = s1
    print(s1)