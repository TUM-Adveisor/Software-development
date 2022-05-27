import games
import player #can be delatet later




def player_hinzufügen():
    pnew=player.Player("otto ")
    print(pnew.name)

def new_game(name):
    print("welches spiel möchtets du spielen")
    Spiel=1 #ergebniss von einlesen
    print("Wie viele Spieler sollen mitspieln können?")
    Playeranzahl=3 #ergebniss von einlesen
    if Spiel==1:
        new_game=games.Monopoly(Playeranzahl)

if __name__ == '__main__':
    l=games.Chess()

    new_spielfeld=[]
    for x in range(85):
            new_spielfeld.append([])
            for y in range(86):
                for j in new_spielfeld:
                        j.append([1,0])
                       

    
   
