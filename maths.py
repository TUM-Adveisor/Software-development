
import numpy as np
class Maths():
    def __init__(self):
        pass
    def abstand_gerade_punkt(self,x1,y1,x2,y2,x3,y3):
        m1=float(x2-x1)
        m2=float(y2-y1)

        t=float((x3-((y3*m1+y1*m1)/m2)-x1)/(2*m1))
        L=[(x3-m1*t),(y3-m1*x3)]
        print (L,t)
    def abstand_punkt_punkt(self,punkt1,punkt2):
        print((punkt1[1]-punkt2[0]))
        print(punkt1[1]**2)
        print(punkt2[0])
        n= ((punkt1[0]-punkt2[0])**2 + (punkt1[1]-punkt2[1])**2)**0.5 #(((punkt1[0]-punkt2[0])**2)+((punkt1[1]-punkt2[1])**2))**0,^5
        print(n)
        return n
m=Maths()
print(m.abstand_punkt_punkt([1,10],[1,100]))