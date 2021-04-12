def ExtractDigits(s):
    def Isdigit(n):
        if ord('0')<=ord(n)<=ord('9'):
            return True
        else:
            return False
        
    n = ''
    for i in s:
        if Isdigit(i):
            n += i
    return n

s = input()
a = ExtractDigits(s)
print(a)