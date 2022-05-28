class Player:
    id=None
    name="OTTO"
    color=None
    Ki=None
    nextplayer=None

    def __init__(self,c,nextplayer=0,n="eric",Ki=0):
        self.name=n
        self.color=c
        self.Ki=Ki
        self.nextplayer=nextplayer
        
    def get_Move(self):
        if self.Ki==1:
            pass #stockfish aufrufen
        else:
            pass #visaul rcognition vom anderen feld anrufen nach änderungen