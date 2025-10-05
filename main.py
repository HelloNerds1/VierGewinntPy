from VierGewinntPy.player import *

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
    
    def __init__(self, spielbrett, row_num, col_num, win = False):
        self.spielbrett = spielbrett
        self.row_num = row_num
        self.col_num = col_num
        self.win = win 
    
    def Spielbrett(self):
        """ Diese Funktion erstellt das Spielbrett. Hierbei werden mehrere Listen in eine Liste 
        zusammengefügt, um eine Matrix zu erstellen. """
        for m in range(self.row_num):
            zeile = []
            for n in range(self.col_num):
                zeile.append(" ")             # Spielbrett mit leeren Einträgen füllen      # av, vllt. Leerzeichen in ASCII?
            spielbrett.append(zeile)

    def Ausgabe(self):
        """ In dieser Funktion wird das Spielbrett für die Konsole formatiert ausgegeben. 
        Dazu wird die Spielbrett Matrix durchgegenagen, wobei für jeden Eintrag ein leeres Feld eingefügt wird. """
        print("0     1     2     3     4     5     6")    # av
        for i in range(self.row_num):
            for j in range(self.col_num):
                print(spielbrett[self.row_num-i-1][j], end="  |  ")   # end bedeutet am Ende jedes Eintrages
            print()     # printe nach jedem vollendeten j sozusagen einen Zeilenumbruch

    def Abfrage(self, spieler):
        """ beschreiben """
        while True:             # SR
            try:
                value = int(input('Spalte eingeben: ')) # Benutzereingabe in Ganzzahl
                global counter 
                global col0
                global col1
                global col2
                global col3
                global col4
                global col5
                global col6
                counter = counter +1

                """ Gedächtinis über die Züge: """
                if value < self.row_num:   # Hier wird gegengespüft, ob die eingegebene Zahl auch innerhalb des Spielfeldes liegt
                    if value == 0:
                        spielbrett[col0][value] = spieler   # hier wird das gewünschte Spieler-Symbol genutzt
                        col0 = col0 +1
                        break
                    if value == 1:
                        spielbrett[col1][value] = spieler
                        col1 = col1 +1
                        break
                    if value == 2:
                        spielbrett[col2][value] = spieler
                        col2 = col2 +1
                        break         
                    if value == 3:
                        spielbrett[col3][value] = spieler
                        col3 = col3 +1      
                        break   
                    if value == 4:
                        spielbrett[col4][value] = spieler
                        col4 = col4 +1    
                        break
                    if value == 5:
                        spielbrett[col5][value] = spieler
                        col5 = col5 +1    
                        break
                    if value == 6:
                        spielbrett[col6][value] = spieler
                        col6 = col6 +1    
                        break  
                    
            except:
                continue # versuche es erneut, gehe zum Anfang der Schleife
             

    def CheckWin(self) -> bool:
        """ beschreiben """
        global win 
        """ horizontal """
        for col in range(self.col_num-3):        # -3 aufgrund der range
            for row in range(self.row_num):
                if(spielbrett[row][col] == spielbrett[row][col+1] == spielbrett[row][col+2] == spielbrett[row][col+3] != " "):
                    print("Gewonnen")
                    return True

        """ vertikal """
        for col in range(self.col_num -3):        
            for row in range(self.row_num -3):
                if(spielbrett[row][col] == spielbrett[row+1][col] == spielbrett[row+2][col] == spielbrett[row+3][col] != " "):
                    print("Gewonnen")
                    return True
    
        """ diagonal hochzu """
        for col in range(self.col_num -3):       
            for row in range(self.row_num -3):
                if(spielbrett[row][col] == spielbrett[row+1][col+1] == spielbrett[row+2][col+2] == spielbrett[row+3][col+3] != " "):
                    print("Gewonnen")  
                    return True

        """ diagonal herunter """
        for col in range(self.col_num):        # SR
            for row in range(self.row_num -3):
                if(spielbrett[row][col] == spielbrett[row+1][col-1] == spielbrett[row+2][col-2] == spielbrett[row+3][col-3] != " "):
                    print("Gewonnen") 
                    return True
        return False
    

        
        
# int main()
# {

""" Settings für Matrix etc. """
spielbrett = []
row_num = 8
col_num = 7
win = False

counter = 0
col0 = 0
col1 = 0
col2 = 0
col3 = 0
col4 = 0
col5 = 0
col6 = 0

""" Instanzen """
vier_gewinnt = VierGewinnt(spielbrett, row_num, col_num)
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


