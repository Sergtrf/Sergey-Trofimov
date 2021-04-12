a = open('input.txt', 'r')
d = a.readlines()
a.close()
for i in d[::-1]:
    print(i[::-1].strip())