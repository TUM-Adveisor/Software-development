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
        
    def get_move(self,recognition):
        if self.Ki==1:
            string=list(stockfish.get_best_move())
            for i in string:
                if i==a:
                    string[i]=1
                elif i==b:
                    string[i]=2
                elif i==c:
                    string[i]=3
                elif i==d:
                    string[i]=4
                elif i==e:
                    string[i]=5
                elif i==f:
                    string[i]=6
                elif i==g:
                    string[i]=7
                elif i==h:
                    string[i]=8
                else:
                    pass
            start=[string[0],string[1]]
            end=[string[2],string[3]]
        else:
            #recognition.get_pos()
            start=[1,1]
            end=[3,6]
        return [start,end,self.nextplayer]
    
    