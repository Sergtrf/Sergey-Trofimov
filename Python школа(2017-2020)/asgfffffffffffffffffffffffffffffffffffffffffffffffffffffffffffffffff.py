n = int(input())
mino1 = 0; mino2 = 0; mino3 = 0
minc1 = [float('inf')]; minc2 = [float('inf')]; minc3 = [float('inf')]
minn = 0
res = 0
for i in range(n):
    a, b, c = map(int, input().split())
    if c <= b and c <= a:
        minn = min((a-c),(b-c))
        if minn % 4 == 1 and  minn // 4 <= minc1[-1]:
            minc1.append(minn // 4)
            mino1 += 1
        if minn % 4 == 2 and minn // 4 <= minc2[-1]:
            minc2.append(minn // 4)
            mino2 += 1
        if minn % 4 == 3 and  minn // 4 <= minc3[-1]:
            minc3.append(minn // 4)
            mino3 += 1
        res += (a + b)
    elif a <= b and a <= c:
        minn = min((b-a),(c-a))
        if minn % 4 == 1 and  minn // 4 <= minc1[-1]:
            minc1.append(minn // 4)
            mino1 += 1
        if minn % 4 == 2 and minn // 4 <= minc2[-1]:
            minc2.append(minn // 4)
            mino2 += 1
        if minn % 4 == 3 and  minn // 4 <= minc3[-1]:
            minc3.append(minn // 4)
            mino3 += 1
        res += (c + b)        
    elif b <= a  and b <= c:
        minn = min((a-b),(c-b))
        if minn % 4 == 1 and  minn // 4 <= minc1[-1]:
            minc1.append(minn // 4)
            mino1 += 1
        if minn % 4 == 2 and minn // 4 <= minc2[-1]:
            minc2.append(minn // 4)
            mino2 += 1
        if minn % 4 == 3 and  minn // 4 <= minc3[-1]:
            minc3.append(minn // 4)
            mino3 += 1
        res += (a + c)
minc1.remove(float('inf'));minc2.remove(float('inf'));minc3.remove(float('inf'))
if res % 4 == 0:
    print(res)
else:
'''
10
3
3
3
3
3
5
7
8
9
3
'''