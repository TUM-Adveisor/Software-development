import games
import player #can be delatet later
import sys
sys.path.insert(1, '/home/pi/Adveisor/Hardware/gcodelib')
import bewegungsystem
b=bewegungsystem.Bewegungssystem()




# time.sleep(5)
# while(True):   
connection.send_coords(130.57575,100)
connection.wait_for_movement_start()
print("header started")
while (connection._status != "Idle"):
    connection.print_coords()
    time.sleep(1/10)
print("header stopped")
time.sleep(0.4)
connection.send_coords(130,180)
connection.wait_for_movement_start()
print("header started")
while (connection._status != "Idle"):
    connection.print_coords()
    time.sleep(1/10)
print("header stopped")
time.sleep(0.4)
connection.send_coords(0,180)
connection.wait_for_movement_start()
print("header started")
while (connection._status != "Idle"):
    connection.print_coords()
    time.sleep(1/10)
print("header stopped")
time.sleep(0.4)
connection.send_coords(0,100)
connection.wait_for_movement_start()
print("header started")
while (connection._status != "Idle"):
    connection.print_coords()
    time.sleep(1/10)
print("header stopped")
time.sleep(0.4)
connection.send_coords(130,100)
connection.wait_for_movement_start()
print("header started")
while (connection._status != "Idle"):
    connection.print_coords()
    time.sleep(1/10)
print("header stopped")
time.sleep(0.4)
connection.send_coords(130,180)
connection.wait_for_movement_start()
print("header started")
while (connection._status != "Idle"):
    connection.print_coords()
    time.sleep(1/10)
print("header stopped")
time.sleep(0.4)


# time.sleep(1)

# connection.send_coords(15,0)
# connection.wait_for_movement_start()
# print("header started")
# while (connection._status != "Idle"):
#     connection.print_coords()
#     time.sleep(1/10)
    # print("header stopped")

# time.sleep(1)

###################
# connection.send_coords(15,0)
# connection.home()
# connection.wait_for_movement_stop()
# magnes.wlacz()
# connection.send_coords(0,0)
# connection.wait_for_movement_stop()
# magnes.wylacz()




    ##################

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
    new_spielfeld=[]
    for x in range(85):
            new_spielfeld.append([])
            for y in range(86):
                for j in new_spielfeld:
                        j.append([1,0])
    l=games.Chess()
    