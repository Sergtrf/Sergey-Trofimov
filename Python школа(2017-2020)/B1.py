a = open('input.txt', 'r')
c = open('output.txt', 'w')
t=list(map(int, a.read().split())) 
l=list(filter(lambda x: x%2 == 0 and x> 0,t))
if l != []:
    print(min(l), max(l), file = c)
else:
    print(0, file = c)
a.close()
c.close()