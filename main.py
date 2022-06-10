import games
import config
import player #can be delatet later

import bewegungsystem
config=config.Config()
b=bewegungsystem.Bewegungssystem(config)


b.bewege_von_nach(400,400,200,000,"test")



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
    #config=config.Config()
    print("Game startet")
    #l=games.Chess(config)
