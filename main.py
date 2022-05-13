
import  games
import piece2



if __name__ == '__main__':
    print("game startet ")
    player_p=piece2.Player_Ledders_and_Snackes
    new_game=games.Ledders_snacks()
    z=new_game.move()
    print(z,"zufallszahl")
   
def new_game():
    print("welches spiel möchtets du spielen")
    Spiel=1 #ergebniss von einlesen
    print("Wie viele Spieler sollen mitspieln können?")
    Playeranzahl=3 #ergebniss von einlesen
    if Spiel==1:
        new_game=games.Monopoly(Playeranzahl)
    