def ToLower (n):
    if ord ('A') <= ord(n) <= ord('Z'):
        return chr(ord(n) - ord('A') + ord('a'))
    else:
        return n
   
def IsPalindrom(n):
    for i in range (len(n)):
        if ord(n[i]) == ord(' '):
            n -= n[i]
    for i in range (0,len(n)//2,1):
        if ord(ToLower(n[i])) != ord(ToLower(n[-i-1])):
            return False
    return True
 
n = input()
if IsPalindrom(n):
    print('YES')
else:
    print('NO')