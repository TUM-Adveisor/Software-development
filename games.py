import random
import player
class Game:
    max_player=None
    min_player=None
    playerlist=[]
    mover=1
    round=1
    kartenset=None
    XY_Matrix=[]
    Scheirichkeitstufe=["computertechnik","linalg","Schaltungstheorie"]

    def __init__(self):
      pass 



class Monopoly(Game):
    def __init__(self,Ap):
        self.max_player=6
        self.kartenset=aktionskarten=[
"Sie kommen aus dem Gefängnis frei! Behalten Sie diese Karte, bis Sie sie benötigen oder verkaufen.",
"Schulgeld. Zahlen Sie M 50.",
"Urlaubsgeld! Sie erhalten M 100.",
"Ihre Lebensversicherung wird fällig. Sie erhalten M 100.", 
"Arzt-Kosten. Zahlen Sie M 50.",
"Einkommenssteuerrückerstattung. Sie erhalten M 20.", 
"Krankenhausgebühren. Zahlen Sie M 100.",
"Gehen Sie in das Gefängnis. Begeben Sie sich direkt dorthin. Gehen Sie nicht über Los. Ziehen Sie nicht M 200 ein.", 
"Sie erhalten auf Vorzugs-Aktien 7% Dividende: M 25.",
"Sie haben Geburtstag. Jeder Spieler schenkt Ihnen M 10.", 
"Sie erben M 100.", 
"Aus Lagerverkäufen erhalten Sie M 50.", 
"Zweiter Preis im Schönheitswettbewerb. Sie erhalten M 10.", 
"Sie werden zu Straßenausbesserungsarbeiten herangezogen. Zahlen Sie M 40 je Haus und M 115 je Hotel an die Bank.", 
"Rücken Sie vor bis auf Los. (Ziehe M 200 ein).", 
"Bank-Irrtum zu Ihren Gunsten. Ziehen Sie M 200 ein.", 
"Rücken Sie vor bis zur Schlossallee.", 
"Machen Sie einen Ausflug zum Südbahnhof. Wenn Sie über Los kommen, ziehen Sie M 200 ein.", 
"Ihr Bausparvertrag wird fällig. Sie erhalten M 200.", 
"Rücken Sie vor bis zum Opernplatz. Wenn Sie über Los kommen, ziehen Sie M 200 ein.", 
"Gehen Sie in das Gefängnis. Begeben Sie sich direkt dorthin. Gehen Sie nicht über Los. Ziehen Sie nicht M 200 ein.", 
"Rücken Sie vor bis auf Los. (Ziehe M 200 ein).", 
"Die Bank zahlt Ihnen eine Dividende von M 50.", 
"Sie lassen Ihre Häuser renovieren. Zahlen Sie: M 25 pro Haus, M 100 pro Hotel.", 
"Sie kommen aus dem Gefängnis frei! Behalten Sie diese Karte, bis Sie sie benötigen oder verkaufen.", 
"Rücken Sie vor bis zur Seestraße. Wenn Sie über Los kommen, ziehen Sie M 200 ein.", 
"Sie sind zum Vorstand gewählt worden. Zahlen Sie jedem Spieler M 50.", 
"Ihr Bausparvertrag wird fällig. Sie erhalten M 200.", 
"Gehen Sie 3 Felder zurück.", 
"Strafzettel! Zahlen Sie M 15.", 
"Rücken Sie vor bis zum nächsten Verkehrsfeld. Der Eigentümer erhält das Doppelte der normalen Miete. Wenn das Verkehrsfeld noch niemandem gehört, können Sie es von der Bank kaufen",
"Rücken Sie vor bis zum nächsten Versorgungswerk. Werfen Sie die Würfel und zahlen dem Eigentümer den zehnfachen Betrag Ihres Wurfergebnisses. Wenn das Werk noch niemandem gehört, können Sie es von der Bank kaufen." ]
        self.min_player=2
        for x in range(11):
            self.XY_Matrix.append([])
            for y in range(11):
                for j in self.XY_Matrix:
                    if y==0 or y==11 or x==0 or x==11:
                        j.append([x,y])
                    else:
                        j.append([0,0])

        for i in range(Ap):
            print("spielername?")
            self.player_hinzufügen()


        if self.max_player>=Ap and self.min_player<=Ap:
            self.playercount=Ap
    
    def aktionskarte_ziehen(self):
        return self.kartenset[random.randint(1,len(self.kartenset))]

    def player_hinzufügen():
        player.Player(name="otto")



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
    def __init__(self,Ap):
        self.max_player=10
        self.min_player=1

        if self.max_player>=Ap and self.min_player<=Ap:
            self.playercount=Ap

        for x in range(12):
            self.XY_Matrix.append([])
            for y in range(12):
                for j in self.XY_Matrix:
                    j.append([x,y])
                
    def roll_the_dice(self):
        print(self.mover)
        self.mover=self.mover+1
        print(self.mover)
        return (random.randint(1,6))
    
    def move(self): 
         
       return self.roll_the_dice()
       print("welche figur beawegen?")


