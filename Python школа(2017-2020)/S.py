def IsSubstring(Pattern, Source):
 step = 0
 
 if len(Pattern)>len(Source): 
  return 'NO'
 
 for i in range(len(Source)):
  for j in range(len(Pattern)):
   if i+j < len(Source):
    if Source[i+j] != Pattern[j]:
     break
   else:
    return 'NO'
  else:
   return 'YES'
 return 'NO'
   

Pattern = input()
Source = input()

print(IsSubstring(Pattern, Source))