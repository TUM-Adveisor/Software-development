
from lib2to3.pgen2.token import OP


class Node:
    def __init__(self,x_pos,y_pos):
        self.g_cost=0 #vom startpunkt entfernt
        self.h_cost=0  #vom endpunkt entfernt
        self.f_cost=self.h_cost+self.g_cost #gesamt costen
        self.neighbours=[]
        self.refrenze=None
        self.parent=None
        self.x_pos=x_pos
        self.y_pos=y_pos
        self.move_coast=0
        self.next_to_move=None
    def calculate_costs(self,c_f,end,l):
        if j.refrenze!=None:
            self.g_cost=c_f.g_cost+self.new_cost(c_f)
            self.h_coast=self.shortest_path_raw_costs(end)
            self._move_coast=self.calculate_move_cost(l)
            self.f_cost=self.g_cost+self.h_costh_cost+self.move_coast
        else:
            self.g_cost=c_f.g_cost+self.new_cost(c_f)
            self.h_coast=self.shortest_path_raw_costs(end)
            self.f_cost=self.g_cost+self.h_costh_cost
    
    def move_path(self,l):
        if self.parent!=None:
            l.append([self.x_pos,self.y_pos])
            self.parent.move_path(l)
        else:
            pass # aufruf vom bewegungssystem
    
    def calculate_move_cost(self,l):
        cost=0
        
        for n in self.neighbours:
            if n.refrenze==None:
                if  n.new_cost*2<cost or cost==0:
                    cost=n.new_cost*2
            else:
                if  n.new_cost*2<cost or cost==0:
                    cost=n.new_cost*2+n.calculate_move_cost()
                    self.next_to_move=n
        
        return cost



    def shortest_path_raw_costs(self,end):
        if self.y_pos!=end.y_pos and self.x_pos!=end.x_pos:
            y=self.y_pos
            x=self.x_pos
            d_counter=0
            while self.y_pos!=end.y_pos and self.x_pos!=end.x_pos:
                d_counter=d_counter+1
                if x<end.x_pos:
                    x=x+1
                    if y<end.y_pos:
                        y=y+1
                    else:
                        y=y-1
                else:
                    x=x-1
                    if y<end.y_pos:
                        y=y+1
                    else:
                        y=y-1
        
            return abs((y-end.y_pos)+(x-end.x_pos))*10+d_counter*14

                
        else:
            return abs((self.y_pos-end.y_pos)+(self.x_pos-end.x_pos))*10

    def new_cost(self,c_f):
        if self.x_pos==c_f.x_pos or self.y_pos==c_f.y_pos:
            return 10
        else:
            return 14
    

way=[]
XY_Matrix=[]
for x in range(8):
            XY_Matrix.append([])
            for y in range(8):  
                n=Node(x,y)                                         
                XY_Matrix[x].append([x,y,n])# 1/1 ist unten links
                


def shortest_path(start,end):
    Open=[start]
    closed=[]
    c_f=Open[0]
    for i in Open:
        if i.f_cost<c_f.f_cost:
            c_f=i
        elif i.f_cost==c_f.f_cost:
            if i.h_cost<c_f.h_cost:
                c_f=i
        else:
            pass
    
    closed.append(c_f)
    Open.remove(c_f)

    if c_f==end:
        c_f.move_path()

    for j in c_f.neighbours:
        if   j in closed:
            continue

        if c_f.f_cost+j.new_cost(c_f,j)<j.f_cost or j not in Open:
            j.calculate_costs(c_f,end)
            j.parrent=c_f
            Open.append(j)
        

            


