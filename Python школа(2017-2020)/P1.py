n = int(input())
if (n%6) == 0:
    print(n//6)
    print(*[6]*(n//6))
elif (n%6) + (n//6) >= 5:
    print(n//6 + 1)
    print(*[6]*((n//6) - 5 + (n%6)), *[5]*(6 - (n%6)))
else:
    print(n//6 + n%6)
    print(*[6]*(n//6), *[1]*(n%6))