
import games
import piece2
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
    l=games.Monopoly(5)
    
   
    
   
    """
    print("game startet "
    player_p=piece2.Player_Ledders_and_Snackes
    new_game=games.Ledders_snacks(5)
    z=new_game.move()
    print(z,"zufallszahl")
    
    print(l.aktionskarte_ziehen())
    z=games.Ledders_snacks(3)
    print(z.XY_Matrix[3][1])

  """##