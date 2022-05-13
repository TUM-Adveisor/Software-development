import random

class Game:
    max_player=None
    min_player=None
    playercount=1
    mover=1
    round=1

    def __init__(self):
        pass

class Monopoly(Game):
    def __init__(self,Ap):
        self.max_player=6
        self.min_player=2
        if self.max_player>=Ap and self.min_player<=Ap:
            self.playercount=Ap
    
    def roll_the_dice(self):
        z1=random.randint(1,6)
        z2=random.randint(1,6)
        
        if z1!=z2:
            self.move=self.move+1
        else:
            self.move=self.move #unacesarry
        return (z1+z2)

    def move(self):
        print("trade?")
        print("use card?")
        print("buy hauses")
        print("skip")
        return self.roll_the_dice

        
      
            
class Ledders_snacks(Game):
    def __init__(self):
        self.max_player=10
        self.min_player=1

    def roll_the_dice(self):
        print(self.mover)
        self.mover=self.mover+1
        print(self.mover)
        return (random.randint(1,6))

    def move(self): 
         
       return self.roll_the_dice()
       print("welche figur beawegen?")


