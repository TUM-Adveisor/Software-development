class Recognition:
    def __init__(self):
        #print("recognition startet" )
        pass
    def get_pos(self,piece_thype,c):
        if piece_thype=='Pawn':
            return [70,90]
        elif piece_thype=='Rook':
            return [130,150]
        elif piece_thype=='Knight':
            return [170,150]
        elif piece_thype=='Bishop':
            return [210,150]
        elif piece_thype=='King':
            return [240,150]
        elif piece_thype=='Queen':
            return [270,150]
        

   