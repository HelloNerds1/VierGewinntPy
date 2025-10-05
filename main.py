#from VierGewinntPy.player import *

class Spieler:
    
    def __init__(self, icon = str):
        self.icon = icon 
   
    def PlayerMessage(self):
        print(f'Spieler {self.icon} ist dran')



class AutoSpieler:
    
    def __init__(self, icon = str):
        self.icon = icon 
   
    def PlayerMessage(self):
        print(f'Spieler {self.icon} ist dran')
    
    def GetTurn(self, Field):
        # wo denkt der Computer, dass es hingehört?
        pass
        


class VierGewinnt():
    
    def __init__(self, row_num, col_num, win = False):
        """ beschreiben """
        self.row_num = row_num
        self.col_num = col_num
        self.win = win 
        # alles was nicht mit übergeben wird:
        self.spielbrett = []
        self.counter = 0
        self.col0 = 0
        self.col1 = 0
        self.col2 = 0
        self.col3 = 0
        self.col4 = 0
        self.col5 = 0
        self.col6 = 0
    
    def Spielbrett(self):
        """ Diese Funktion erstellt das Spielbrett. Hierbei werden mehrere Listen in eine Liste 
        zusammengefügt, um eine Matrix zu erstellen. """
        for m in range(self.row_num):
            zeile = []
            for n in range(self.col_num):
                zeile.append(" ")             # Spielbrett mit leeren Einträgen füllen      # av, vllt. Leerzeichen in ASCII?
            self.spielbrett.append(zeile)

    def Ausgabe(self):
        """ In dieser Funktion wird das Spielbrett für die Konsole formatiert ausgegeben. 
        Dazu wird die Spielbrett Matrix durchgegenagen, wobei für jeden Eintrag ein leeres Feld eingefügt wird. """
        print("0     1     2     3     4     5     6")    # av
        for i in range(self.row_num):
            for j in range(self.col_num):
                print(self.spielbrett[self.row_num-i-1][j], end="  |  ")   # end bedeutet am Ende jedes Eintrages
            print()     # printe nach jedem vollendeten j sozusagen einen Zeilenumbruch

    def Abfrage(self, spieler):
        """ beschreiben """
        while True:             # SR
            try:
                value = int(input('Spalte eingeben: ')) # Benutzereingabe in Ganzzahl
                global counter 
                #col0
                #col1
                #col2
                #col3
                #col4
                #col5
                #col6
                counter = counter +1

                """ Gedächtinis über die Züge: """
                if value < self.row_num:   # Hier wird gegengespüft, ob die eingegebene Zahl auch innerhalb des Spielfeldes liegt
                    if value == 0:
                        self.spielbrett[self.col0][value] = spieler   # hier wird das gewünschte Spieler-Symbol genutzt
                        self.col0 = self.col0 +1
                        break
                    if value == 1:
                        self.spielbrett[self.col1][value] = spieler
                        self.col1 = self.col1 +1
                        break
                    if value == 2:
                        self.spielbrett[self.col2][value] = spieler
                        self.col2 = self.col2 +1
                        break         
                    if value == 3:
                        self.spielbrett[self.col3][value] = spieler
                        self.col3 = self.col3 +1      
                        break   
                    if value == 4:
                        self.spielbrett[self.col4][value] = spieler
                        self.col4 = self.col4 +1    
                        break
                    if value == 5:
                        self.spielbrett[self.col5][value] = spieler
                        self.col5 = self.col5 +1    
                        break
                    if value == 6:
                        self.spielbrett[self.col6][value] = spieler
                        self.col6 = self.col6 +1    
                        break  
                    
            except:
                continue # versuche es erneut, gehe zum Anfang der Schleife
             

    def CheckWin(self) -> bool:
        """ beschreiben """
        global win 
        """ horizontal """
        for col in range(self.col_num-3):        # -3 aufgrund der range
            for row in range(self.row_num):
                if(self.spielbrett[row][col] == self.spielbrett[row][col+1] == self.spielbrett[row][col+2] == self.spielbrett[row][col+3] != " "):
                    print("Gewonnen")
                    return True

        """ vertikal """
        for col in range(self.col_num -3):        
            for row in range(self.row_num -3):
                if(self.spielbrett[row][col] == self.spielbrett[row+1][col] == self.spielbrett[row+2][col] == self.spielbrett[row+3][col] != " "):
                    print("Gewonnen")
                    return True
    
        """ diagonal hochzu """
        for col in range(self.col_num -3):       
            for row in range(self.row_num -3):
                if(self.spielbrett[row][col] == self.spielbrett[row+1][col+1] == self.spielbrett[row+2][col+2] == self.spielbrett[row+3][col+3] != " "):
                    print("Gewonnen")  
                    return True

        """ diagonal herunter """
        for col in range(self.col_num):        # SR
            for row in range(self.row_num -3):
                if(self.spielbrett[row][col] == self.spielbrett[row+1][col-1] == self.spielbrett[row+2][col-2] == self.spielbrett[row+3][col-3] != " "):
                    print("Gewonnen") 
                    return True
        return False
    

        
        
# int main()
# {

""" Settings """
row_num = 8
col_num = 7
win = False
counter = 0


""" Instanzen """
vier_gewinnt = VierGewinnt(row_num, col_num)
player1 = Spieler("x")
player2 = Spieler("o")


""" Spielschleife """
board = vier_gewinnt.Spielbrett()        # Erstellt die Matrix die als Spielbrett genutzt wird
ausgeben = vier_gewinnt.Ausgabe() 

while win != True:
    if (counter % 2) == 0:
        player1.PlayerMessage()
        abfrage = vier_gewinnt.Abfrage(player1.icon)
        ausgeben = vier_gewinnt.Ausgabe() 
        win = vier_gewinnt.CheckWin()
    elif (counter % 2) == 1:
        player2.PlayerMessage()
        abfrage = vier_gewinnt.Abfrage(player2.icon)
        ausgeben = vier_gewinnt.Ausgabe() 
        win = vier_gewinnt.CheckWin()


"""Testbereich"""

# return 0; 
# }

# :)


