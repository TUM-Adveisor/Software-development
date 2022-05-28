class piece:
    color=None
    size=None #durchmesser in mm
    x_pos_real=None
    y_pos_real=None
    
    def __init__(self,color,x_pos_real,y_pos_real):
        self.y_pos_real=y_pos_real
        self.x_pos_real=x_pos_real
        if color==0:
            self.color=="weiß"
        elif color==1:
            self.color=="black"
        elif color==2:
            self.color="red"
        

class Player_Monopoly(piece):
    def __init__(self):
        self.x_pos=0
        self.y_pos=0
        self.size=25

class Player_Ledders_and_Snackes(piece):
    def __init__(self):
        self.x_pos=0
        self.y_pos=0
        self.size=40

class Pawn(piece):
    def __init__(self,color,x_pos_real,y_pos_real):
        super().__init__(color,x_pos_real,y_pos_real)
        self.size=30

class Rook(piece):
    def __init__(self,color,x_pos_real,y_pos_real):
        super().__init__(color,x_pos_real,y_pos_real)
        self.size=30

class Knight(piece):
    def __init__(self,color,x_pos_real,y_pos_real):
        super().__init__(color,x_pos_real,y_pos_real)
        self.size=30
class Bishop(piece):
    def __init__ (self,color,x_pos_real,y_pos_real):
        super().__init__(color,x_pos_real,y_pos_real)
        self.size=30

class King(piece):
    def __init__(self, color,x_pos_real,y_pos_real):
        super().__init__(color,x_pos_real,y_pos_real)
        self.size=30
        
class Queen(piece):
    def __init__(self, color,x_pos_real,y_pos_real):
        super().__init__(color,x_pos_real,y_pos_real)
        self.size=30     
		