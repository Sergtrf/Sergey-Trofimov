from math import *
from tkinter import *

def II(x): return I1 + int((x - X1)*(I2 - I1)/(X2 - X1))

def JJ(y): return J2 + int((y - Y1)*(J1 - J2)/(Y2 - Y1))

def F(x):
    if x == 0: f = 1
    else: f = sin(x)/x
    return f

print("Введите размер осей")
X2, Y2 = map(int,input().split())
X1, Y1 = -X2, -Y2
I1 = 0; J1 = 0
I2 = 50 * X2; J2 = 50 * Y2
n = 5000
h = (X2 - X1)/n
root = Tk()
root.title('График функции F(x)')

canv = Canvas(root, width = I2 + 100,height = J2 + 100, bg = 'white')
canv.create_line(I2//2 + 50, 50, I2//2 + 50, J2 + 50,width = 2)
canv.create_line(50, J2//2 + 50,I2 + 50, J2//2 + 50,width = 2)
points = []
k = -X2; k2 = -Y2
for i in range(50, J2 + 75, 25):
    canv.create_line((I2 + 100)//2 - 3, i, (I2 + 100)//2 + 3, i, width = 2)
    if k != 0: canv.create_text((I2 + 100)//2 + 10, i, text = str(k))
    k += 1
for i in range(50, I2 + 75, 25):
    canv.create_line(i, (J2 + 100)//2 - 3, i, (J2 + 100)//2 + 3, width = 2)
    if k2 != 0: canv.create_text(i, (J2 + 100)//2 + 10, text = str(k2))
    k2 += 1
x = X1
for i in range(n):
    y = F(x)
    P = (II(x) + 50,JJ(y) + 50)
    points.append(P)
    x = x + h
canv.create_line(points,width = 1, fill = 'red', smooth = 1)
canv.create_text(J2 + 50, (I2 + 100)//2 - 10,text = "X")
canv.create_text((J2 + 100)//2 - 10, 50, text = "Y")
canv.pack()
root.mainloop()
