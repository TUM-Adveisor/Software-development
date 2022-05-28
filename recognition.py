class Recognition:
    def __init__(self):
        print("recognition startet" )

    def get_x_pos(self,piece_thype):
        if piece_thype=='Pawn':
            return 1
        elif piece_thype=='Rook':
            return 2
        elif piece_thype=='Knight':
            return 3
        elif piece_thype=='Bishop':
            return 4
        elif piece_thype=='King':
            return 5
        elif piece_thype=='Queen':
            return 6
        

    def get_y_pos(self,piece_thype):
        if piece_thype=='Pawn':
            return 1
        elif piece_thype=='Rook':
            return 2
        elif piece_thype=='Knight':
            return 3
        elif piece_thype=='Bishop':
            return 4
        elif piece_thype=='King':
            return 5
        elif piece_thype=='Queen':
            return 6