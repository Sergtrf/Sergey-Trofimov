def Eval(s):
   l = len(s)
     
start = 0
el1 = 0
zn = '+'
 
for i in range(l):
   if s[i] =='+' or s[i] == '-':
      if zn == '+':
         el1 += int(s[start:i])
      elif zn == '-':
         el1 -= int(s[start:i])
         zn = s[i]
         start = i+1
         if zn == '+':
            el1 += int(s[start:])
         elif zn == '-':
            el1 -= int(s[start:])
            return el1
 
s = input()
print(Eval(s))