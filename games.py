import recognition
import bewegungsystem
import math
import random
import player
import piece2
class Game:
    max_player=None
    min_player=None
    playerlist=[]
    piecelist=[]
    recognition=None
    mover=1
    round=1
    kartenset=None
    XY_Matrix=[]
    Schwirichkeitstufe=None
    pnew=None
    toleranz=1# abstand den figuren mindestens beim anernander vorbeizihen haben sollen
    bewegungsytem=None
    feldgröße_y=None
    feldgröße_x=None
    felderstart_x=None
    felderstart_y=None

    def __init__(self):
      pass 

    def shortest_move(self,x_start,y_start,x_end,y_end,piece):
        
        for i in self.piecelist:
            h1=self.piecelist[i].x_pos
            h2=self.piecelist[i].y_pos
            d=self.abstand_punkt_gerade(x_start, y_start,x_end, y_end, h1, h2)
            if d<=(self.piecelist[i].size+piece.size)/2+self.tolernaz:
                self.suche_nächste_lücke(x_start,y_start,x_end,y_end,self.piecelist[i])
            else:
                self.movement(x_start,y_start,x_end,y_end)# funktion um figur tatzächlich zu bewegen

    def suche_nächste_lücke(self,x_start,y_start,x_end,y_end,piece):
        for i in self.piecelist:
            h1=self.piecelist[i].x_pos
            h2=self.piecelist[i].y_pos
            d=self.abstand_punkt_gerade(x_start, y_start,x_end, y_end, h1, h2)
    
            
    

            
    def abstand_punkt_gerade(self,x_start,y_start,x_end,y_end,h1,h2): #liefert falsche ergebnisse
        m=[x_end-x_start,y_end-y_start]
        lam=(-y_start*m[1]-x_start*m[0]+h1*m[0]+h2+m[1])/((m[0]**2)+(m[1]**2))
        s1=x_start+lam*m[0]
        s2=y_start+lam*m[1]

        d=self.hypotenusen_länge(s1,s2,h1,h2)
        return d

        
    
    def hypotenusen_länge(self,x_start,y_start,x_end,y_end):
        h=math.sqrt(((x_end-x_start)**2)+((y_end-y_start)**2))
        return h

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
            #input einfügen
            n="input"+str(i)
            self.playerlist.append(self.player_hinzufügen(n))

            


        if self.max_player>=Ap and self.min_player<=Ap:
            self.playercount=Ap
        else:pass #Fehler werfen einfügen
    
    def aktionskarte_ziehen(self):
        return self.kartenset[random.randint(1,len(self.kartenset))]

    def player_hinzufügen(self,name):
       pnew=player.Player(name)
       return pnew
       



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


class Chess(Game):
    def __init__(self):
        self.bewegungsytem=bewegungsystem.Bewegungssystem()
        self.recognition=recognition.Recognition()
        self.max_player=2
        self.min_player=2
        self.feldgröße_y=40
        self.feldgröße_x=40
        self.felderstart_x=70
        self.felderstart_y=90
        for x in range(8):
            self.XY_Matrix.append([])
            for y in range(8): 
                print(self.XY_Matrix)                                            
                p_new=self.add_piece(x+1,y+1)
                self.XY_Matrix[x].append([x,y])# 1/1 ist unten links
                self.piecelist.append(p_new)
    
        

        self.playerlist.append (self.new_player())
        self.playerlist.append (self.new_player(self.playerlist[0]))
        self.playerlist[0].nextplayer=self.playerlist[1]
        S=int(input("gebe für schwierichkeitstufe Computertechnik 1 ,für Linare Algebra 2 oder für Schaltungstheorie 3 an: "))
        Schwierichkeitstufen_Liste=["Computertechnik","Linare Algebra","Schaltungstheorie"]
        self.Schwirichkeitstufe=Schwierichkeitstufen_Liste[S]
        
    
    def new_player(self,nex_player=0):
        t=len(self.playerlist) 
        if t==0:
            c=0
        else:
            c=1
        name=str(input("name des pielers:  "))
        Ki=int(input("soll der spieler eine Ki sein, bitte antworten sie mit 1 falls ja und 0 falls nein:  "))
        return player.Player(c,name,Ki)

        

    def add_piece(self,x_pos, y_pos):
        c=1
        if y_pos<=2:
            c=0  #0 steht für weiß

        if y_pos==2 or y_pos==7:
    
            pos_real=self.recognition.get_pos('Pawn',c)
            
            new_pos_real=self.logic_to_real_postion(x_pos,y_pos)
            self.bewegungsytem.bewege_von_nach(pos_real[0],pos_real[1],new_pos_real[0],new_pos_real[1],"test") #richtige positionen einfügen
            new_p=piece2.Pawn(c,new_pos_real[0],new_pos_real[1])
            return new_p

        elif y_pos==1:
            if x_pos==1 or x_pos==8:
                pos_real=self.recognition.get_pos('Rook',c) # aufruf der visual rcognition um an positionsdaten zu kommen
                new_pos_real=self.logic_to_real_postion(x_pos,y_pos)
                self.bewegungsytem.bewege_von_nach(pos_real[0],pos_real[1],new_pos_real[0],new_pos_real[1],"test") #richtige positionen einfü
                new_p=piece2.Rook(c,new_pos_real[0],new_pos_real[1])
                return new_p
            elif x_pos==2 or x_pos==7:
                pos_real=self.recognition.get_pos('Knight',c)
                new_pos_real=self.logic_to_real_postion(x_pos,y_pos)
                self.bewegungsytem.bewege_von_nach(pos_real[1],pos_real[0],new_pos_real[0],new_pos_real[1],"test") #richtige positionen einfü
                new_p=piece2.Knight(c,new_pos_real[0],new_pos_real[1])
            elif x_pos==3 or x_pos==6:
                pos_real=self.recognition.get_pos('Bishop',c)
                new_pos_real=self.logic_to_real_postion(x_pos,y_pos)
                self.bewegungsytem.bewege_von_nach(pos_real[0],pos_real[1],new_pos_real[0],new_pos_real[1],"test") #richtige positionen einfü
                new_p=piece2.Bishop(c,new_pos_real[0],new_pos_real[1])
                return new_p
            elif x_pos==4:
                pos_real=self.recognition.get_pos('King',c)
                new_pos_real=self.logic_to_real_postion(x_pos,y_pos)
                self.bewegungsytem.bewege_von_nach(pos_real[0],pos_real[1],new_pos_real[0],new_pos_real[1],"test") #richtige positionen einfü
                p_new=piece2.King(c,pos_real[0],new_pos_real[1])
                return p_new
            else:
                pos_real=self.recognition.get_pos('Queen',c)
                new_pos_real=self.logic_to_real_postion(x_pos,y_pos)
                self.bewegungsytem.bewege_von_nach(pos_real[0],pos_real[1],new_pos_real[0],new_pos_real[1],"test") #richtige positionen einfü
                p_new=piece2.Queen(c,new_pos_real[0],new_pos_real[1])
                return p_new
            
    def real_to_logic_postion(self,x_pos,y_pos):
        höhe_feld=self.feldgröße_x
        breite_feld=self.feldgröße_y

        for i in range(8):
        
            if y_pos // höhe_feld<i:
                y_pos=i
        
        for i in range(8):
            print(i)
            if x_pos // breite_feld <i:
                x_pos=i
        return[x_pos,y_pos]

    def logic_to_real_postion(self,x_pos,y_pos):

        real_postion_y=self.felderstart_x+((y_pos)*self.feldgröße_y)
        real_postion_x=self.felderstart_x+((x_pos)*self.feldgröße_x)
    
        return [real_postion_x,real_postion_y]
       

    def move():
        pass







