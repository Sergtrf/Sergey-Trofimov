n = int(input())
ch1 = 0
ch2 = 0
maxs = 0
ost1 = 0; ost2 = 0
for i in range(n):
   x = int(input()); y = x%180
   if ch2 >= ch1:
      if y!=ost2 and x > ch1:
            if ch2%7!=0 and x%7==0:
               ch1 = x
               maxs = ch1 + ch2
               ost1 = y
            elif ch2%7==0:
               ch1 = x
               maxs = ch1 + ch2
               ost1 = y
      elif y!=ost1 and x > ch2:
         if ch1%7!=0 and x%7 == 0:
            ch2 = x 
            maxs = ch1 + ch2
            ost2 = y
         elif ch1%7 == 0:
            ch2 = x
            maxs = ch1 + ch2
            ost2 = y
   elif ch1 >= ch2:
      if y!=ost1 and x > ch2:
            if ch1%7!=0 and x%7==0:
               ch2 = x
               maxs = ch1 + ch2
               ost2 = y
            elif ch1%7==0:
               ch2 = x
               maxs = ch1 + ch2
               ost2 = y
      elif y!=ost2 and x > ch1:
            if ch2%7!=0 and x%7 == 0:
               ch1 = x 
               maxs = ch1 + ch2
               ost1 = y
            elif ch2%7 == 0:
               ch1 = x
               maxs = ch1 + ch2
               ost1 = y
if ch1 == 0 or ch2 == 0:
   print(0,0)
else:
   print(ch1, ch2)