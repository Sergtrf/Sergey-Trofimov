from math import *
from tkinter import *
k= int(input())
root = Tk()
canv = Canvas(root, width = 600,height = 600, bg = 'lightblue')
x1,y1 = map(int, input().split())
x2,y2 = map(int, input().split())
def Gen(x1,y1,x2,y2,k):
   if k == 0:
      return
   l=int(sqrt((x2-x1)**2+(y2-y1)**2))
   h = l/(2*sqrt(3))
   x3 = x1 +int((x2-x1)/3+0.5)
   y3 = y1 +int((y2- y1)/3 +0.5)
   x4 = x1 +int(2*(x2-x1)/3+0.5)
   y4 = y1 +int(2*(y2- y1)/3 +0.5)
   x5 = int((x2+x1)/2+(h*(y2-y1)/l))
   y5 = int((y2+y1)/2+(h*(x2-x1)/l))          
   canv.create_line(x1, y1,x3,y3 , width =2)
   canv.create_line( x3, y3,x5,y5 , width =2)
   canv.create_line( x5, y5,x4,y4 , width =2,smooth = 1)
   canv.create_line( x4, y4,x2,y2 , width =2,smooth = 1)
   canv.create_line( x3, y3,x4,y4 , width =3, fill = 'lightblue')
   Gen(x1, y1,x3,y3, k-1)
   Gen(x3, y3,x5,y5 ,k-1)
   Gen(x5, y5,x4,y4 ,k-1)
   Gen(x4, y4,x2,y2 ,k-1)
 
Gen(x1,y1,x2,y2,5) 
canv.pack()
root.mainloop()