def Toint(n):
    k=0
    for i in range(0,len(n),1):
        k += 10**(len(n)-i-1)*(ord(n[i])-ord('0'))
    return k

def GetSideAndStep (n):
    for i in range (len(n)):
        if n[i] == ' ':
            step = n[i + 1 :]
            side = n[: i]
            break
    return step, side

def Treasure ():
    x, y = 0, 0
    l = input()
    while l != 'Treasure!':
        step, side = GetSideAndStep(l)
        if side == 'East':
            x += Toint(step)
        elif side == 'West':
            x -= Toint(step)
        elif side == 'South':
            y -= Toint(step)
        else:
            y += Toint(step)
        l = input()
    return x, y

d, f = Treasure()
print(d,f)
