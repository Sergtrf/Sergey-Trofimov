def bukva(n):
    if ord ('A')<=ord(n)<=ord('Z'):
        return True
    elif ord('a')<=ord(n)<=ord('z'):
        return True
    else:
        return False
    
def CountWords(n):
    k = 0
    l = 0
    for i in range(0,len(n),1):
        if bukva (n[i]):
            l += 1
            if l == 1:
                k += 1
        else:
            l = 0
    return k
    
n = input()
print (CountWords(n))