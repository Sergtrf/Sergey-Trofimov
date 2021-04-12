def ToLower (n):
    if ord ('A') <= ord(n) <= ord('Z'):
        return chr(ord(n) - ord('A') + ord('a'))
    else:
        return n

def whithoutSPACE(n):
    k = ''
    for i in range(len(n)):
        if ord(n[i]) != ord(' '):
            k += n[i]
    n = k
    return n
   
def IsPalindrom(n):
    for i in range (0,len(n)//2,1):
        if ord(ToLower(n[i])) != ord(ToLower(n[-i-1])):
            return False
    return True
 
n = input()
n = whithoutSPACE(n)
if IsPalindrom(n):
    print('yes')
else:
    print('no')