n=input()
n2=input()
if(ord(n2)>ord(n)):
    for i in range (ord(n),ord(n2)+1,1):
        print(chr(i),end=' ')
        else:
            for i in range (ord(n),128,1):
                print(chr(i),end=' ')
            for i in range (0,ord(n2)+1,1):
                print(chr(i), end=' ')
