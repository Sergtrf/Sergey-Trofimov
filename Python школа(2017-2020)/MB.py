import math
n = math.radians(int(input()))
x = 0
if 5 <= math.degrees(n) <= 85:
    x += ((800*800*math.cos(n)*math.cos(n)*math.sin(n))/9.8) + ((0.000813669*800*800*800*800*math.sin(n)*math.sin(n)*math.cos(n)*math.cos(n))/(9.8*9.8))
    print(x)
else:
    print('False')