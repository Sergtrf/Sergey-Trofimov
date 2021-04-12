a = open('input.txt', 'r')
d = a.read()
a.close()
print(d[::-1])